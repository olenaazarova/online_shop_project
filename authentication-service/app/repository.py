from app.database import connection


def create_credentials(email: str, password_hash: str) -> dict:
    with connection() as conn:
        row = conn.execute(
            """
            INSERT INTO auth_users (email, password_hash)
            VALUES (%s, %s)
            RETURNING id::text, email, created_at
            """,
            (email.lower(), password_hash),
        ).fetchone()
    return {"id": row[0], "email": row[1], "created_at": row[2].isoformat()}


def find_by_email(email: str) -> dict | None:
    with connection() as conn:
        row = conn.execute(
            """
            SELECT id::text, email, password_hash, created_at
            FROM auth_users
            WHERE email = %s
            """,
            (email.lower(),),
        ).fetchone()

    if not row:
        return None

    return {
        "id": row[0],
        "email": row[1],
        "password_hash": row[2],
        "created_at": row[3].isoformat(),
    }


def find_by_id(user_id: str) -> dict | None:
    with connection() as conn:
        row = conn.execute(
            """
            SELECT id::text, email, created_at
            FROM auth_users
            WHERE id = %s
            """,
            (user_id,),
        ).fetchone()

    if not row:
        return None

    return {"id": row[0], "email": row[1], "created_at": row[2].isoformat()}


def delete_by_id(user_id: str) -> None:
    with connection() as conn:
        conn.execute("DELETE FROM auth_users WHERE id = %s", (user_id,))
