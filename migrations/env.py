"""Alembic migrations environment — delegates to app/alembic_env.py"""
import sys
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.alembic_env import run_migrations_offline, run_migrations_online
from alembic import context

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
