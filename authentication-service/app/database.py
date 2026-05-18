import time
from contextlib import contextmanager

import psycopg

from app.settings import settings


def initialize_database() -> None:
    for attempt in range(1, 21):
        try:
            with connection() as conn:
                conn.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS auth_users (
                        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                        email TEXT UNIQUE NOT NULL,
                        password_hash TEXT NOT NULL,
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
