"""
extractor.py — BookingScraper Pro v49
Fixes applied:
  BUG-014 / SCRAP-BUG-014: BeautifulSoup parser falls back gracefully.
  BUG-107 / SCRAP-BUG-007: Language detection tries multiple strategies.
  NEW-EXTRACT-001         : _extract_json_ld() — schema.org Hotel data extraction
                            (main_image_url, short_description, rating_value, best_rating,
                            review_count_schema, street_address, address_locality,
                            address_country, postal_code).
  NEW-EXTRACT-002         : _extract_hotel_photos_js() — parse hotelPhotos JS variable
                            for full photo metadata (id_photo, orientation, dimensions, alt,
                            all 3 size URLs: thumb_url, large_url, highres_url).
  Platform               : Windows 11 compatible (no POSIX deps).
"""

from __future__ import annotations

import json
import logging
import re
from typing import Any, Dict, List, Optional, Tuple

from bs4 import BeautifulSoup, FeatureNotFound

from app.config import get_settings

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Parser selection — BUG-014 / SCRAP-BUG-014 fix
# ---------------------------------------------------------------------------

def _make_soup(html: str) -> BeautifulSoup:
    """
    Create BeautifulSoup with lxml, falling back to html.parser.
    BUG-014 fix: lxml is preferred for speed but html.parser (stdlib)
    is always available as a fallback.
    """
    for parser in ("lxml", "html.parser"):
        try:
            return BeautifulSoup(html, parser)
        except FeatureNotFound:
            logger.debug("Parser '%s' unavailable, trying next.", parser)
    return BeautifulSoup(html, "html.parser")


# ---------------------------------------------------------------------------
# Language detection — BUG-107 fix: multi-strategy
# ---------------------------------------------------------------------------

_LANG_META_PATTERNS: List[re.Pattern] = [
    re.compile(r'<html[^>]+lang=["\']([a-z]{2}(?:-[a-z]{2,4})?)["\']', re.IGNORECASE),
    re.compile(r'<meta[^>]+http-equiv=["\']content-language["\'][^>]+content=["\']([a-z]{2}(?:-[a-z]{2,4})?)["\']', re.IGNORECASE),
    re.compile(r'<meta[^>]+content=["\']([a-z]{2}(?:-[a-z]{2,4})?)["\'][^>]+http-equiv=["\']content-language["\']', re.IGNORECASE),
]


def detect_language(html: str, url: str = "") -> Optional[str]:
    """
    Detect the content language of an HTML page using multiple strategies.

    Strategy order:
    1. <html lang="xx"> attribute
    2. <meta http-equiv="Content-Language"> tag
    3. URL language path component (e.g. /hotel.es.html → 'es')
    4. og:locale meta tag
    5. Return None if undetermined
    """
    if not html:
        return None

    for pattern in _LANG_META_PATTERNS:
        match = pattern.search(html[:2000])
        if match:
            lang = match.group(1).lower()[:2]
            logger.debug("Language detected via meta/html-attr: %s", lang)
            return lang

    try:
        soup = _make_soup(html[:5000])
        og_locale = soup.find("meta", attrs={"property": "og:locale"})
        if og_locale and og_locale.get("content"):
            lang = str(og_locale["content"]).lower()[:2]
            logger.debug("Language detected via og:locale: %s", lang)
            return lang

        meta_lang = soup.find("meta", attrs={"name": re.compile(r"^language$", re.I)})
        if meta_lang and meta_lang.get("content"):
            lang = str(meta_lang["content"]).lower()[:2]
            logger.debug("Language detected via meta[name=language]: %s", lang)
            return lang

    except Exception as exc:
        logger.debug("Language detection via BeautifulSoup failed: %s", exc)

    if url:
        url_lang = _lang_from_url(url)
        if url_lang:
            logger.debug("Language detected via URL: %s", url_lang)
            return url_lang

    logger.debug("Language undetermined for URL: %s", url)
    return None


def _lang_from_url(url: str) -> Optional[str]:
    """Extract ISO 639-1 code from Booking.com URL path pattern."""
    match = re.search(r"\.([a-z]{2})(?:-[a-z]{2,4})?\.html", url, re.IGNORECASE)
    if match:
        return match.group(1).lower()
    return None


# ---------------------------------------------------------------------------
# hotelPhotos JS extraction helper (module-level for reuse)
# ---------------------------------------------------------------------------

def extract_hotel_photos_from_html(html: str) -> List[Dict[str, Any]]:
    """
    Parse the `hotelPhotos` JavaScript variable embedded in Booking.com HTML.

    Returns a list of photo dicts with keys:
      id_photo    : str  — Booking.com photo ID
      thumb_url   : str  — max200 URL (with k= auth token)
      large_url   : str  — max1024x768 URL
      highres_url : str  — max1280x900 URL
      alt         : str  — image alt text
      orientation : str  — 'landscape' | 'portrait' | 'square'
      created     : str  — creation timestamp string
      photo_width : int  — original width in pixels
      photo_height: int  — original height in pixels

    NEW-EXTRACT-002: Extracts from inline JS, NOT from <img> tags,
    so all size URLs and full auth params (k=...) are preserved.
    """
    photos: List[Dict[str, Any]] = []
    if not html:
        return photos

    # Match hotelPhotos: [{ ... }] — greedy but bounded by the outer array
    # The JS block can span thousands of lines; use re.DOTALL
    match = re.search(
        r'hotelPhotos\s*:\s*(\[(?:[^[\]]|\[(?:[^[\]]|\[[^\[\]]*\])*\])*\])',
        html,
        re.DOTALL,
    )
    if not match:
        # Fallback pattern for slightly different formatting
        match = re.search(
            r'"hotelPhotos"\s*:\s*(\[.+?\])\s*(?:,|\})',
            html,
            re.DOTALL,
        )
    if not match:
        logger.debug("hotelPhotos JS variable not found in HTML")
        return photos

    raw_array = match.group(1)

    # Clean JS → valid JSON:
    # 1. Single quotes → double quotes (JS uses both)
    # 2. Unquoted keys → quoted keys
    # 3. Trailing commas (invalid JSON) → remove
    try:
        # Replace single-quoted string values with double-quoted
        cleaned = re.sub(r"'([^']*)'", r'"\1"', raw_array)
        # Quote unquoted JS keys: word: → "word":
        cleaned = re.sub(r'(?<!["\w])(\b[a-zA-Z_]\w*\b)\s*:', r'"\1":', cleaned)
        # Remove trailing commas before } or ]
        cleaned = re.sub(r',\s*([}\]])', r'\1', cleaned)
        parsed = json.loads(cleaned)
    except (json.JSONDecodeError, Exception) as exc:
        logger.debug("hotelPhotos JSON parse failed (primary): %s", exc)
        # Second attempt: individual object extraction via regex
        parsed = _extract_photo_objects_regex(raw_array)

    for obj in parsed:
        if not isinstance(obj, dict):
            continue
        photo: Dict[str, Any] = {}

        # Required: photo ID
        pid = obj.get("id") or obj.get("id_photo")
        if not pid:
            continue
        photo["id_photo"] = str(pid).strip()

        # Size URLs — must include query params (k= auth token)
        for key in ("thumb_url", "large_url", "highres_url"):
            val = obj.get(key, "")
            if val and isinstance(val, str) and "bstatic.com" in val:
                photo[key] = val.strip()

        # Alt text
        photo["alt"] = str(obj.get("alt", "")).strip() or None

        # Orientation
        orient = str(obj.get("orientation", "")).strip().lower()
        photo["orientation"] = orient if orient in ("landscape", "portrait", "square") else None

        # Creation timestamp
        photo["created"] = str(obj.get("created", "")).strip() or None

        # Dimensions — nested under grid: { photo_width, photo_height }
        grid = obj.get("grid") or {}
        if isinstance(grid, dict):
            try:
                photo["photo_width"] = int(grid.get("photo_width", 0)) or None
            except (TypeError, ValueError):
                photo["photo_width"] = None
            try:
                photo["photo_height"] = int(grid.get("photo_height", 0)) or None
            except (TypeError, ValueError):
                photo["photo_height"] = None

        # Only add if we have at least one usable URL
        if any(photo.get(k) for k in ("thumb_url", "large_url", "highres_url")):
            photos.append(photo)

    logger.debug("hotelPhotos extraction: %d photos parsed", len(photos))
    return photos


def _extract_photo_objects_regex(raw: str) -> List[Dict[str, Any]]:
    """
    Fallback: extract individual photo objects from raw JS using regex
    when full JSON parsing fails.
    """
    objects: List[Dict[str, Any]] = []
    # Find each photo object block { ... }
    for block_match in re.finditer(r'\{([^{}]+)\}', raw, re.DOTALL):
        block = block_match.group(1)
        obj: Dict[str, Any] = {}
        # Extract key: 'value' or key: "value" pairs
        for kv in re.finditer(r"""(\w+)\s*:\s*['"]([^'"]*?)['"]""", block):
            obj[kv.group(1)] = kv.group(2)
        # Extract numeric values: key: 12345
        for kv in re.finditer(r'(\w+)\s*:\s*(\d+)', block):
            if kv.group(1) not in obj:
                try:
                    obj[kv.group(1)] = int(kv.group(2))
                except ValueError:
                    pass
        if obj.get("id") or obj.get("id_photo"):
            objects.append(obj)
    return objects


# ---------------------------------------------------------------------------
# Data extractors
# ---------------------------------------------------------------------------

class HotelExtractor:
    """Extract structured hotel data from Booking.com HTML."""

    def __init__(self, html: str, url: str = "", language: str = "en") -> None:
        self.html = html
        self.soup = _make_soup(html)
        self.url = url
        self.language = language
        self._cfg = get_settings()

    def extract_all(self) -> Dict[str, Any]:
        """
        Extract all available hotel fields and return as dict.
        NEW-EXTRACT-001: includes JSON-LD schema.org enrichment fields.
        """
        # Base fields
        data: Dict[str, Any] = {
            "url": self.url,
            "language": self.language,
            "hotel_name": self._extract_name(),
            "address": self._extract_address(),
            "description": self._extract_description(),
            "review_score": self._extract_review_score(),
            "review_count": self._extract_review_count(),
            "star_rating": self._extract_star_rating(),
            "city": self._extract_city(),
            "country": self._extract_country(),
            "latitude": self._extract_latitude(),
            "longitude": self._extract_longitude(),
            "amenities": self._extract_amenities(),
            "photos": self._extract_photo_urls(),
        }

        # NEW-EXTRACT-001: merge schema.org JSON-LD data
        json_ld = self._extract_json_ld()
        if json_ld:
            data.update(json_ld)

        return {k: v for k, v in data.items() if v is not None}

    def extract_hotel_photos(self) -> List[Dict[str, Any]]:
        """
        NEW-EXTRACT-002: Extract full hotelPhotos metadata from HTML JS.
        Returns list of photo dicts (id_photo, thumb_url, large_url, highres_url,
        alt, orientation, photo_width, photo_height, created).
        Called separately from extract_all() since photos are hotel-level data
        (language-independent) and only extracted for 'en' language.
        """
        return extract_hotel_photos_from_html(self.html)

    # ── JSON-LD / schema.org extraction ──────────────────────────────────────

    def _extract_json_ld(self) -> Dict[str, Any]:
        """
        NEW-EXTRACT-001: Parse schema.org Hotel JSON-LD embedded in the page.

        Extracts:
          main_image_url     — Hotel.image (primary photo URL)
          short_description  — Hotel.description (short summary)
          rating_value       — aggregateRating.ratingValue
          best_rating        — aggregateRating.bestRating
          review_count_schema — aggregateRating.reviewCount
          street_address     — address.streetAddress
          address_locality   — address.addressLocality
          address_country    — address.addressCountry
          postal_code        — address.postalCode
        """
        result: Dict[str, Any] = {}
        try:
            for tag in self.soup.find_all("script", attrs={"type": "application/ld+json"}):
                raw = tag.string or ""
                if not raw.strip():
                    continue
                try:
                    ld = json.loads(raw)
                except json.JSONDecodeError:
                    continue

                # Handle @graph arrays
                if isinstance(ld, dict) and ld.get("@graph"):
                    candidates = ld["@graph"]
                elif isinstance(ld, list):
                    candidates = ld
                else:
                    candidates = [ld]

                for item in candidates:
                    if not isinstance(item, dict):
                        continue
                    if item.get("@type") not in ("Hotel", "LodgingBusiness", "Accommodation"):
                        continue

                    # Primary image
                    image = item.get("image")
                    if image and isinstance(image, str) and image.startswith("http"):
                        result["main_image_url"] = image

                    # Short description
                    desc = item.get("description", "")
                    if desc and isinstance(desc, str) and desc.strip():
                        result["short_description"] = desc.strip()

                    # aggregateRating
                    rating = item.get("aggregateRating") or {}
                    if isinstance(rating, dict):
                        rv = rating.get("ratingValue")
                        if rv is not None:
                            try:
                                result["rating_value"] = float(rv)
                            except (TypeError, ValueError):
                                pass
                        br = rating.get("bestRating")
                        if br is not None:
                            try:
                                result["best_rating"] = float(br)
                            except (TypeError, ValueError):
                                pass
                        rc = rating.get("reviewCount")
                        if rc is not None:
                            try:
                                result["review_count_schema"] = int(rc)
                            except (TypeError, ValueError):
                                pass

                    # address
                    addr = item.get("address") or {}
                    if isinstance(addr, dict):
                        sa = addr.get("streetAddress", "")
                        if sa:
                            result["street_address"] = str(sa).strip()[:512]
                        al = addr.get("addressLocality", "")
                        if al:
                            result["address_locality"] = str(al).strip()[:256]
                        ac = addr.get("addressCountry", "")
                        if ac:
                            result["address_country"] = str(ac).strip()[:128]
                        pc = addr.get("postalCode", "")
                        if pc:
                            result["postal_code"] = str(pc).strip()[:20]

                    # Found a Hotel item — stop searching
                    if result:
                        logger.debug("JSON-LD extracted: %d fields", len(result))
                        return result

        except Exception as exc:
            logger.debug("JSON-LD extraction error: %s", exc)

        return result

    # ── Existing extractors (unchanged) ──────────────────────────────────────

    def _safe_text(self, selector_result: Any) -> Optional[str]:
        if selector_result is None:
            return None
        try:
            text = selector_result.get_text(strip=True)
            return text[:self._cfg.MAX_ERROR_LEN] if text else None
        except Exception:
            return None

    def _extract_name(self) -> Optional[str]:
        for selector in [
            {"attrs": {"data-testid": "title"}},
            {"class_": re.compile(r"pp-header__title", re.I)},
            {"id": "hp_hotel_name"},
        ]:
            el = self.soup.find(True, **selector)  # type: ignore
            if el:
                return self._safe_text(el)
        for tag in self.soup.find_all(["h1", "h2"], limit=5):
            text = self._safe_text(tag)
            if text and len(text) > 3:
                return text
        return None

    def _extract_address(self) -> Optional[str]:
        el = self.soup.find(attrs={"data-testid": "address"})
        return self._safe_text(el)

    def _extract_description(self) -> Optional[str]:
        el = self.soup.find(attrs={"data-testid": "property-description"})
        if el:
            return self._safe_text(el)
        el = self.soup.find("div", {"id": "property_description_content"})
        return self._safe_text(el)

    def _extract_review_score(self) -> Optional[float]:
        try:
            el = self.soup.find(attrs={"data-testid": "review-score"})
            if el:
                text = el.get_text(strip=True)
                match = re.search(r"(\d+[.,]\d+)", text)
                if match:
                    return float(match.group(1).replace(",", "."))
        except Exception as exc:
            logger.debug("review_score extraction failed: %s", exc)
        return None

    def _extract_review_count(self) -> Optional[int]:
        try:
            patterns = [
                re.compile(r"(\d[\d,\.]+)\s*review", re.IGNORECASE),
                re.compile(r"(\d[\d,\.]+)\s*opinion", re.IGNORECASE),
                re.compile(r"(\d[\d,\.]+)\s*Bewertung", re.IGNORECASE),
            ]
            text = self.soup.get_text()
            for pattern in patterns:
                match = pattern.search(text)
                if match:
                    count_str = match.group(1).replace(",", "").replace(".", "")
                    return int(count_str)
        except Exception as exc:
            logger.debug("review_count extraction failed: %s", exc)
        return None

    def _extract_star_rating(self) -> Optional[float]:
        try:
            el = self.soup.find(attrs={"data-testid": "rating-stars"})
            if el:
                stars = el.find_all("svg")
                return float(len(stars)) if stars else None
        except Exception:
            pass
        return None

    def _extract_city(self) -> Optional[str]:
        try:
            breadcrumbs = self.soup.find_all(attrs={"data-testid": re.compile(r"breadcrumb")})
            if len(breadcrumbs) >= 2:
                return self._safe_text(breadcrumbs[-2])
        except Exception:
            pass
        return None

    def _extract_country(self) -> Optional[str]:
        try:
            breadcrumbs = self.soup.find_all(attrs={"data-testid": re.compile(r"breadcrumb")})
            if breadcrumbs:
                return self._safe_text(breadcrumbs[0])
        except Exception:
            pass
        return None

    def _extract_latitude(self) -> Optional[float]:
        try:
            el = self.soup.find("a", {"data-atlas-latlng": True})
            if el:
                latlng = el["data-atlas-latlng"].split(",")
                return float(latlng[0])
        except Exception:
            pass
        return None

    def _extract_longitude(self) -> Optional[float]:
        try:
            el = self.soup.find("a", {"data-atlas-latlng": True})
            if el:
                latlng = el["data-atlas-latlng"].split(",")
                return float(latlng[1]) if len(latlng) > 1 else None
        except Exception:
            pass
        return None

    def _extract_amenities(self) -> List[str]:
        try:
            els = self.soup.find_all(attrs={"data-testid": "facility-list-item"})
            return [self._safe_text(el) for el in els if self._safe_text(el)]
        except Exception:
            return []

    def _extract_photo_urls(self) -> List[str]:
        """
        Extract plain photo URLs from <img> tags.
        Used as fallback when hotelPhotos JS is unavailable.
        NOTE: This method does NOT strip query params — BUG-IMG-401 is fixed
        at the Selenium extraction level in scraper.py.
        """
        try:
            imgs = self.soup.find_all("img", attrs={"data-testid": re.compile(r"photo", re.I)})
            urls = []
            for img in imgs:
                src = img.get("src") or img.get("data-src")
                if src and src.startswith("http") and "bstatic.com" in src:
                    urls.append(src)
            return urls[:50]
        except Exception:
            return []
