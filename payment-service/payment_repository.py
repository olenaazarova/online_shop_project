import os
import time

import psycopg


DATABASE_URL = os.getenv("DATABASE_URL", "")


def initialize_database() -> None:
    if not DATABASE_URL:
        return

    for attempt in range(1, 21):
        try:
            with psycopg.connect(DATABASE_URL, autocommit=True) as conn:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS payments (
                        id BIGSERIAL PRIMARY KEY,
                        user_id INTEGER NOT NULL,
                        payment_id INTEGER UNIQUE NOT NULL,
                        amount NUMERIC(12, 2) NOT NULL,
                        item TEXT NOT NULL,
                        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                    )
                    """
                )
            return
        except psycopg.OperationalError:
            if attempt == 20:
                raise
            time.sleep(1.5)


def save_payment(payment) -> None:
    if not DATABASE_URL:
        return

    with psycopg.connect(DATABASE_URL, autocommit=True) as conn:
        conn.execute(
            """
            INSERT INTO payments (user_id, payment_id, amount, item)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (payment_id) DO UPDATE
            SET amount = EXCLUDED.amount,
                item = EXCLUDED.item
            """,
            (payment.user_id, payment.payment_id, payment.amount, payment.item),
        )
