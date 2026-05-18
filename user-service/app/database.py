import time
from contextlib import contextmanager

import psycopg

from app.settings import settings


def initialize_database() -> None:
    for attempt in range(1, 21):
        try:
            with connection() as conn:
                try:
                    conn.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")
                except psycopg.errors.UniqueViolation:
                    pass
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS user_profiles (
                        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                        auth_user_id UUID UNIQUE NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        phone TEXT,
                        role TEXT NOT NULL DEFAULT 'customer',
                        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                    )
                    """
                )
            return
        except psycopg.OperationalError:
            if attempt == 20:
                raise
            time.sleep(1.5)


@contextmanager
def connection():
    with psycopg.connect(settings.database_url, autocommit=True) as conn:
        yield conn
