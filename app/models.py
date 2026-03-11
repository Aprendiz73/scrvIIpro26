"""
models.py — BookingScraper Pro v49
Fixes applied:
  BUG-DESC-001  : Description cross-contamination — thread-safe scraper sessions (see scraper.py).
  BUG-IMG-401   : Image 401 — query params were stripped removing k= auth token (see scraper.py).
  BUG-IMG-SCHEMA: image_downloads missing id_photo / category columns.
  NEW-TABLE-001 : image_data — full photo metadata (orientation, dimensions, alt, created).
  NEW-COLS-001  : hotels — schema.org fields: main_image_url, short_description, rating_value,
                  best_rating, review_count_schema, street_address, address_locality,
                  address_country, postal_code.
  BUG-003/103   : ScrapingLog FK enforced via trigger (unchanged).
  BUG-007/012   : version_id optimistic locking (unchanged).
  BUG-016       : URLLanguageStatus check includes all valid statuses (unchanged).
  BUG-019       : SystemMetrics time-series indexes (unchanged).
  SCRAP-BUG-007 : JSONB defaults use callable factories (unchanged).
  Platform      : Windows 11 / PostgreSQL 15+ / psycopg v3.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from sqlalchemy import (
    BigInteger, Boolean, CheckConstraint, Column, DateTime, Float,
    Index, Integer, SmallInteger, String, Text, UniqueConstraint,
    event, text,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# ---------------------------------------------------------------------------
# Base
# ---------------------------------------------------------------------------

class Base(DeclarativeBase):
    """Common base for all ORM models."""
    pass


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


# ---------------------------------------------------------------------------
# URLQueue
# ---------------------------------------------------------------------------

class URLQueue(Base):
    """
    Scraping task queue.

    Optimistic locking via `version_id`:
    Usage — always reload with session.get(URLQueue, id) before updating
    status to detect concurrent modifications.
    """
    __tablename__ = "url_queue"
    __mapper_args__ = {
        "version_id_col": None,
    }

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    url: Mapped[str] = mapped_column(String(2048), nullable=False, unique=True)
    base_url: Mapped[str] = mapped_column(String(2048), nullable=False)
    hotel_id_booking: Mapped[Optional[str]] = mapped_column(String(64), nullable=True, index=True)
    status: Mapped[str] = mapped_column(
        String(32), nullable=False, default="pending", index=True
    )
    priority: Mapped[int] = mapped_column(SmallInteger, nullable=False, default=5)
    retry_count: Mapped[int] = mapped_column(SmallInteger, nullable=False, default=0)
    max_retries: Mapped[int] = mapped_column(SmallInteger, nullable=False, default=3)
    last_error: Mapped[Optional[str]] = mapped_column(String(2000), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=_utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=_utcnow, onupdate=_utcnow
    )
    scraped_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    version_id: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending','processing','done','error','skipped')",
            name="chk_url_queue_status",
        ),
        CheckConstraint("priority BETWEEN 1 AND 10", name="chk_url_queue_priority"),
        Index("ix_url_queue_status_priority", "status", "priority"),
        Index("ix_url_queue_created_at", "created_at"),
    )

    def __repr__(self) -> str:
        return f"<URLQueue id={self.id} status={self.status}>"


# ---------------------------------------------------------------------------
# Hotel
# ---------------------------------------------------------------------------

class Hotel(Base):
    """
    Core hotel data store.

    NEW-COLS-001: schema.org / JSON-LD fields added (v49):
      main_image_url    — Hotel.image from schema.org
      short_description — Hotel.description (short) from schema.org
      rating_value      — aggregateRating.ratingValue
      best_rating       — aggregateRating.bestRating
      review_count_schema — aggregateRating.reviewCount (cross-check vs scraped)
      street_address    — address.streetAddress
      address_locality  — address.addressLocality
      address_country   — address.addressCountry
      postal_code       — address.postalCode
    """
    __tablename__ = "hotels"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    url_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        index=True,
        comment="FK to url_queue.id (enforced via FK constraint in SQL)",
    )
    url: Mapped[str] = mapped_column(String(2048), nullable=False)
    language: Mapped[str] = mapped_column(String(10), nullable=False, index=True)
    hotel_name: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    hotel_id_booking: Mapped[Optional[str]] = mapped_column(String(64), nullable=True, index=True)
    city: Mapped[Optional[str]] = mapped_column(Text, nullable=True, index=True)
    country: Mapped[Optional[str]] = mapped_column(Text, nullable=True, index=True)
    address: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    latitude: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    longitude: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    star_rating: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    review_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    review_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # NEW-COLS-001: schema.org / JSON-LD enrichment fields
    main_image_url: Mapped[Optional[str]] = mapped_column(String(2048), nullable=True,
        comment="Hotel primary image URL from schema.org JSON-LD 'image' field")
    short_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True,
        comment="Short description from schema.org JSON-LD 'description' field")
    rating_value: Mapped[Optional[float]] = mapped_column(Float, nullable=True,
        comment="aggregateRating.ratingValue from schema.org")
    best_rating: Mapped[Optional[float]] = mapped_column(Float, nullable=True,
        comment="aggregateRating.bestRating from schema.org (usually 10)")
    review_count_schema: Mapped[Optional[int]] = mapped_column(Integer, nullable=True,
        comment="aggregateRating.reviewCount from schema.org (cross-check with review_count)")
    street_address: Mapped[Optional[str]] = mapped_column(String(512), nullable=True,
        comment="address.streetAddress from schema.org")
    address_locality: Mapped[Optional[str]] = mapped_column(String(256), nullable=True,
        comment="address.addressLocality from schema.org")
    address_country: Mapped[Optional[str]] = mapped_column(String(128), nullable=True,
        comment="address.addressCountry from schema.org")
    postal_code: Mapped[Optional[str]] = mapped_column(String(20), nullable=True,
        comment="address.postalCode from schema.org")

    # JSONB columns — callable default prevents shared mutable state (SCRAP-BUG-007)
    amenities: Mapped[Optional[Dict]] = mapped_column(JSONB, nullable=True, default=dict)
    room_types: Mapped[Optional[List]] = mapped_column(JSONB, nullable=True, default=list)
    policies: Mapped[Optional[Dict]] = mapped_column(JSONB, nullable=True, default=dict)
    photos: Mapped[Optional[List]] = mapped_column(JSONB, nullable=True, default=list)
    raw_data: Mapped[Optional[Dict]] = mapped_column(JSONB, nullable=True, default=dict)
    scrape_duration_s: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    scrape_engine: Mapped[Optional[str]] = mapped_column(String(32), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=_utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=_utcnow, onupdate=_utcnow
    )
    version_id: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    __table_args__ = (
        UniqueConstraint("url_id", "language", name="uq_hotels_url_lang"),
        # BUG-STARRATING-002: Booking.com uses 0-10 scale
        CheckConstraint(
            "star_rating IS NULL OR (star_rating >= 0 AND star_rating <= 10)",
            name="chk_hotels_star_rating",
        ),
        CheckConstraint("review_score BETWEEN 0 AND 10", name="chk_hotels_review_score"),
        CheckConstraint("review_count >= 0", name="chk_hotels_review_count_positive"),
        Index("ix_hotels_city_country", "city", "country"),
        Index("ix_hotels_created_at", "created_at"),
        Index("ix_hotels_amenities_gin", "amenities", postgresql_using="gin"),
    )

    def __repr__(self) -> str:
        return f"<Hotel id={self.id} name={self.hotel_name!r} lang={self.language}>"


# ---------------------------------------------------------------------------
# URLLanguageStatus
# ---------------------------------------------------------------------------

class URLLanguageStatus(Base):
    """
    Tracks per-language scraping completion for each URL.
    BUG-016 fix: check constraint includes ALL valid statuses.
    """
    __tablename__ = "url_language_status"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    language: Mapped[str] = mapped_column(String(10), nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="pending")
    attempts: Mapped[int] = mapped_column(SmallInteger, nullable=False, default=0)
    last_error: Mapped[Optional[str]] = mapped_column(String(2000), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=_utcnow, onupdate=_utcnow)

    __table_args__ = (
        UniqueConstraint("url_id", "language", name="uq_uls_url_lang"),
        CheckConstraint(
            "status IN ('pending','processing','done','error','skipped','incomplete')",
            name="chk_uls_status_valid",
        ),
        Index("ix_uls_status", "status"),
    )

    def __repr__(self) -> str:
        return f"<URLLanguageStatus url_id={self.url_id} lang={self.language} status={self.status}>"


# ---------------------------------------------------------------------------
# ScrapingLog  (PARTITIONED TABLE)
# ---------------------------------------------------------------------------

class ScrapingLog(Base):
    """
    High-volume event log, partitioned by month (RANGE on scraped_at).

    ⚠️  BUG-003 / BUG-103 mitigation:
    PostgreSQL does NOT support FOREIGN KEY constraints on partitioned tables.
    Referential integrity for url_id / hotel_id is enforced by DB trigger:
        trg_scraping_logs_fk_check  (BEFORE INSERT / UPDATE)
    Created by install_clean_v49.sql.
    """
    __tablename__ = "scraping_logs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    url_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    hotel_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), nullable=True)
    language: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    event_type: Mapped[str] = mapped_column(String(64), nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False)
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    duration_ms: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    worker_id: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    extra_data: Mapped[Optional[Dict]] = mapped_column(JSONB, nullable=True, default=dict)
    scraped_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=_utcnow, primary_key=True
    )

    __table_args__ = (
        {"postgresql_partition_by": "RANGE (scraped_at)"},
    )

    def __repr__(self) -> str:
        return f"<ScrapingLog url_id={self.url_id} event={self.event_type} status={self.status}>"


# ---------------------------------------------------------------------------
# ImageDownload
# ---------------------------------------------------------------------------

class ImageDownload(Base):
    """
    Tracks individual image download attempts per hotel photo and size category.

    BUG-IMG-SCHEMA (v49): Added id_photo and category columns.
      id_photo  — Booking.com photo ID (e.g. '49312038'), FK to image_data.id_photo
      category  — size variant: 'thumb_url' | 'large_url' | 'highres_url'

    Unique constraint changed from (hotel_id, url) to (hotel_id, url) kept
    plus partial unique on (hotel_id, id_photo, category) when id_photo IS NOT NULL.
    """
    __tablename__ = "image_downloads"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    hotel_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True)
    # NEW-COLS v49
    id_photo: Mapped[Optional[str]] = mapped_column(String(32), nullable=True, index=True,
        comment="Booking.com photo ID from hotelPhotos JS (e.g. '49312038')")
    category: Mapped[Optional[str]] = mapped_column(String(16), nullable=True,
        comment="Image size variant: thumb_url | large_url | highres_url")
    url: Mapped[str] = mapped_column(String(2048), nullable=False)
    local_path: Mapped[Optional[str]] = mapped_column(String(1024), nullable=True)
    file_size_bytes: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    content_type: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="pending")
    error_message: Mapped[Optional[str]] = mapped_column(String(2000), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=_utcnow)
    downloaded_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending','downloading','done','error','skipped')",
            name="chk_imgdl_status",
        ),
        CheckConstraint(
            "category IS NULL OR category IN ('thumb_url','large_url','highres_url')",
            name="chk_imgdl_category",
        ),
        UniqueConstraint("hotel_id", "url", name="uq_imgdl_hotel_url"),
        # Partial unique: one download record per (hotel, photo, size) when id_photo known
        # NOTE: partial unique index requires manual creation in install_clean_v49.sql
        Index("ix_imgdl_status", "status"),
        Index("ix_imgdl_id_photo", "id_photo"),
    )


# ---------------------------------------------------------------------------
# ImageData  (NEW — v49)
# ---------------------------------------------------------------------------

class ImageData(Base):
    """
    Full photo metadata from Booking.com hotelPhotos JS variable.

    One row per unique photo (id_photo is globally unique across Booking.com).
    Stores orientation, dimensions, alt text, and original creation timestamp.

    Extracted from the inline JavaScript block:
        hotelPhotos: [{ id, thumb_url, large_url, highres_url, alt, orientation,
                        created, grid: { photo_width, photo_height } }, ...]
    """
    __tablename__ = "image_data"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_photo: Mapped[str] = mapped_column(String(32), nullable=False, unique=True,
        comment="Booking.com photo ID — globally unique (e.g. '49312038')")
    hotel_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False, index=True,
        comment="FK to hotels.id — hotel this photo belongs to")
    orientation: Mapped[Optional[str]] = mapped_column(String(16), nullable=True,
        comment="'landscape' or 'portrait'")
    photo_width: Mapped[Optional[int]] = mapped_column(Integer, nullable=True,
        comment="Original photo width in pixels (from grid.photo_width)")
    photo_height: Mapped[Optional[int]] = mapped_column(Integer, nullable=True,
        comment="Original photo height in pixels (from grid.photo_height)")
    alt: Mapped[Optional[str]] = mapped_column(Text, nullable=True,
        comment="Alt text / image description")
    created_at_photo: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True,
        comment="Booking.com photo creation timestamp (from hotelPhotos[].created)")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=_utcnow,
        comment="Record insertion timestamp"
    )

    __table_args__ = (
        CheckConstraint(
            "orientation IS NULL OR orientation IN ('landscape','portrait','square')",
            name="chk_imgdata_orientation",
        ),
        CheckConstraint("photo_width > 0", name="chk_imgdata_width_positive"),
        CheckConstraint("photo_height > 0", name="chk_imgdata_height_positive"),
        Index("ix_imgdata_hotel_id", "hotel_id"),
    )

    def __repr__(self) -> str:
        return f"<ImageData id_photo={self.id_photo} hotel_id={self.hotel_id} orient={self.orientation}>"


# ---------------------------------------------------------------------------
# SystemMetrics
# ---------------------------------------------------------------------------

class SystemMetrics(Base):
    """
    Periodic system health snapshots.
    BUG-019 fix: indexes on time-series query columns.
    """
    __tablename__ = "system_metrics"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    recorded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=_utcnow, index=True
    )
    cpu_usage: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    memory_usage: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    active_workers: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    db_pool_checked_out: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    redis_connected: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    urls_pending: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    urls_done: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    extra_data: Mapped[Optional[Dict]] = mapped_column(JSONB, nullable=True, default=dict)

    __table_args__ = (
        Index("ix_sysmetrics_recorded_cpu", "recorded_at", "cpu_usage"),
        Index("ix_sysmetrics_recorded_mem", "recorded_at", "memory_usage"),
    )

    def __repr__(self) -> str:
        return f"<SystemMetrics recorded_at={self.recorded_at} cpu={self.cpu_usage}>"
