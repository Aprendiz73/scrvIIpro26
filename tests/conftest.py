"""
conftest.py — Shared pytest fixtures for BookingScraper Pro v48.
Runs without a real database — uses SQLite in-memory for ORM tests.
"""

from __future__ import annotations

import os
import pytest
from unittest.mock import MagicMock, patch


@pytest.fixture(autouse=True)
def _reset_settings():
    """Reset settings singleton between tests to avoid state leakage."""
    from app.config import reset_settings
    reset_settings()
    yield
    reset_settings()


@pytest.fixture()
def mock_env(monkeypatch):
    """Provide a minimal valid environment for settings tests."""
    env = {
        "SECRET_KEY": "test-secret-key-that-is-long-enough-for-validation-purposes",
        "DB_USER": "test_user",
        "DB_PASSWORD": "test_password",
        "DB_NAME": "test_db",
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "REDIS_URL": "redis://localhost:6379/0",
        "VPN_ENABLED": "false",
        "ENABLED_LANGUAGES": "es,en,de",
    }
    for k, v in env.items():
        monkeypatch.setenv(k, v)
    return env


@pytest.fixture()
def in_memory_db():
    """
    SQLite in-memory engine for ORM structure tests.
    Does NOT require PostgreSQL to be running.
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from app.models import Base

    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    engine.dispose()


@pytest.fixture()
def mock_redis():
    """Mock Redis client that simulates SET NX and ping."""
    r = MagicMock()
    r.set.return_value = True
    r.ping.return_value = True
    r.delete.return_value = 1
    return r


@pytest.fixture()
def sample_html():
    """Minimal Booking.com-like hotel HTML for extractor tests."""
    return """
    <html lang="es">
    <head>
        <meta property="og:locale" content="es_ES" />
        <title>Hotel Test - Booking.com</title>
    </head>
    <body>
        <h2 data-testid="title">Hotel Corralejo Beach</h2>
        <span data-testid="address">Calle Mayor 1, Corralejo, Fuerteventura</span>
        <div data-testid="review-score">
            <div class="score">8.5</div>
            <span>1,234 reviews</span>
        </div>
        <div data-testid="property-description">
            Beautiful hotel on the beach with stunning ocean views.
        </div>
    </body>
    </html>
    """
