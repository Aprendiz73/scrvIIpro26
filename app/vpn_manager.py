"""
BookingScraper/app/vpn_manager.py
Gestor VPN unificado - BookingScraper Pro
Windows 11 + Python 3.14.3

CORRECCIONES v1.1:
  [FIX] En Windows, usa NordVPNManagerWindows (no comandos Linux)
  [FIX] __del__: seguro contra AttributeError si __init__ falla
  [FIX] Método verify_connection() ahora delega correctamente
  [NEW] Fábrica vpn_manager_factory() → devuelve la clase correcta por SO

CORRECCIONES v2.0 [NEW-09, NEW-14]: ver inline [FIX ...] comments.
"""

import platform
import random
import subprocess
import time
from typing import Dict, Optional

import requests
from loguru import logger


def vpn_manager_factory(interactive: bool = False):
    """
    Fábrica: devuelve el manager correcto según el sistema operativo.

    Args:
        interactive: Si True, permite prompts al usuario.
                     Usar False en tareas Celery.

    Returns:
        NordVPNManagerWindows en Windows, NordVPNManagerLinux en Linux.
    """
    if platform.system() == "Windows":
        from app.vpn_manager_windows import NordVPNManagerWindows
        return NordVPNManagerWindows(method="auto", interactive=interactive)
    else:
        return NordVPNManager()  # Fallback Linux


class NordVPNManager:
    """
    Gestor NordVPN para Linux/Mac.
    En Windows usa vpn_manager_windows.NordVPNManagerWindows.
    """

    def __init__(
        self,
        countries: list = None,
        max_connections_per_server: int = 50,
    ):
        self.countries = countries or ["US", "UK", "DE", "FR", "NL", "ES", "IT", "CA"]
        self.current_server: Optional[str] = None
        self.current_ip:     Optional[str] = None
        self.connection_count = 0
        self.max_connections_per_server = max_connections_per_server

        logger.info(f"VPN Manager (Linux) | países: {', '.join(self.countries)}")

    # ── CONEXIÓN ──────────────────────────────────────────────────────────────

    def connect(self, country: Optional[str] = None) -> bool:
        if country is None:
            country = random.choice(self.countries)
        try:
            logger.info(f"Conectando NordVPN a {country}...")
            self.disconnect()
            time.sleep(2)

            result = subprocess.run(
                ["nordvpn", "connect", country],
                capture_output=True, text=True, timeout=60
            )

            if result.returncode == 0 or "connected" in result.stdout.lower():
                self.current_server = country
                self.connection_count = 0
                time.sleep(5)
                self.current_ip = self.get_current_ip()
                # [NEW-09] Advertir cuando no se pudo obtener la IP — conexión VPN incierta
                if self.current_ip == "Unknown":
                    logger.warning(
                        f"⚠️ Conectado a {country} pero IP externa no verificable. "
                        "Todos los servicios de IP fallaron. La VPN puede no estar activa."
                    )
                else:
                    logger.success(f"✓ Conectado a {country} — IP: {self.current_ip}")
                return True
            else:
                logger.error(f"✗ Error conectando: {result.stderr.strip()}")
                return False

        except subprocess.TimeoutExpired:
            logger.error("✗ Timeout al conectar (60s)")
            return False
        except Exception as e:
            logger.error(f"✗ Error: {e}")
            return False

    # ── DESCONEXIÓN ───────────────────────────────────────────────────────────

    def disconnect(self) -> None:
        try:
            subprocess.run(
                ["nordvpn", "disconnect"],
                capture_output=True, text=True, timeout=30, check=False
            )
            self.current_server = None
            self.current_ip = None
            logger.info("VPN desconectada")
        except Exception as e:
            logger.warning(f"Error desconectando: {e}")

    # ── ROTACIÓN ──────────────────────────────────────────────────────────────

    def rotate(self) -> bool:
        logger.info("🔄 Rotando VPN...")
        self.disconnect()
        time.sleep(3)
        available = [c for c in self.countries if c != self.current_server]
        new_country = random.choice(available) if available else random.choice(self.countries)
        success = self.connect(new_country)
        if success:
            logger.success(f"✓ Rotación exitosa → {new_country}")
        return success

    def auto_rotate_if_needed(self) -> bool:
        self.connection_count += 1
        if self.connection_count >= self.max_connections_per_server:
            logger.warning(f"⚠️ Límite ({self.max_connections_per_server}) alcanzado")
            return self.rotate()
        return False

    # ── VERIFICACIÓN ──────────────────────────────────────────────────────────

    def get_current_ip(self) -> str:
        """
        [NEW-09] Intenta obtener la IP pública desde múltiples servicios.
        Registra un warning si todos fallan en lugar de retornar "Unknown" silenciosamente.
        """
        _ip_services = [
            "https://api.ipify.org?format=text",
            "https://ifconfig.me/ip",
            "https://icanhazip.com",
            "https://ipinfo.io/ip",
        ]
        for service in _ip_services:
            try:
                resp = requests.get(service, timeout=10)
                if resp.status_code == 200:
                    ip = resp.text.strip()
                    if ip:
                        return ip
            except Exception as _ip_err:
                logger.debug(f"  IP service {service} no disponible: {_ip_err}")
                continue
        logger.warning(
            "⚠️ [NEW-09] No se pudo determinar IP pública — todos los servicios fallaron. "
            "Retornando 'Unknown'. Verificar conectividad."
        )
        return "Unknown"

    def verify_connection(self) -> bool:
        """✅ FIX: usa nordvpn status, maneja error correctamente."""
        try:
            result = subprocess.run(
                ["nordvpn", "status"],
                capture_output=True, text=True, timeout=10
            )
            if "connected" not in result.stdout.lower():
                logger.warning("⚠️ VPN no conectada según nordvpn status")
                return False
            test_ip = self.get_current_ip()
            if test_ip == "Unknown":
                logger.warning("⚠️ No se pudo verificar IP externa")
                return False
            logger.info(f"✓ VPN verificada — IP: {test_ip}")
            return True
        except Exception as e:
            logger.error(f"✗ Error verificando VPN: {e}")
            return False

    def reconnect_if_disconnected(self) -> bool:
        if not self.verify_connection():
            logger.warning("🔄 VPN caída, reconectando...")
            return self.connect(self.current_server)
        return True

    def get_status(self) -> Dict[str, object]:  # [NEW-14]
        try:
            result = subprocess.run(
                ["nordvpn", "status"],
                capture_output=True, text=True, timeout=10
            )
            return {
                "connected":        "connected" in result.stdout.lower(),
                "server":           self.current_server,
                "ip":               self.current_ip,
                "connection_count": self.connection_count,
                "status_output":    result.stdout,
            }
        except Exception as e:
            return {
                "connected": False,
                "server":    None,
                "ip":        None,
                "error":     str(e),
            }

    # ── CONTEXT MANAGER ───────────────────────────────────────────────────────

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def __del__(self):
        """✅ FIX: Seguro aunque __init__ haya fallado a medias."""
        try:
            if getattr(self, "current_server", None):
                self.disconnect()
        except Exception:
            pass
