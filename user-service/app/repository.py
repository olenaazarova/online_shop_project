from app.database import connection


def create_profile(profile: dict) -> dict:
    with connection() as conn:
        row = conn.execute(
            """
            INSERT INTO user_profiles (auth_user_id, email, first_name, last_name, phone)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id::text, auth_user_id::text, email, first_name, last_name,
                      phone, role, created_at, updated_at
            """,
            (
                profile["auth_user_id"],
                profile["email"].lower(),
                profile["first_name"],
                profile["last_name"],
                profile.get("phone"),
            ),
        ).fetchone()
    return to_profile(row)


def find_by_auth_user_id(auth_user_id: str) -> dict | None:
    with connection() as conn:
        row = conn.execute(
            """
            SELECT id::text, auth_user_id::text, email, first_name, last_name,
                   phone, role, created_at, updated_at
            FROM user_profiles
            WHERE auth_user_id = %s
            """,
            (auth_user_id,),
        ).fetchone()
    return to_profile(row) if row else None


def update_profile(auth_user_id: str, data: dict) -> dict | None:
    with connection() as conn:
        row = conn.execute(
            """
            UPDATE user_profiles
            SET first_name = COALESCE(%s, first_name),
                last_name = COALESCE(%s, last_name),
                phone = COALESCE(%s, phone),
                updated_at = NOW()
            WHERE auth_user_id = %s
            RETURNING id::text, auth_user_id::text, email, first_name, last_name,
                      phone, role, created_at, updated_at
            """,
            (data.get("first_name"), data.get("last_name"), data.get("phone"), auth_user_id),
        ).fetchone()
    return to_profile(row) if row else None


def to_profile(row) -> dict:
    return {
        "id": row[0],
        "auth_user_id": row[1],
        "email": row[2],
        "first_name": row[3],
        "last_name": row[4],
        "phone": row[5],
        "role": row[6],
        "created_at": row[7].isoformat(),
        "updated_at": row[8].isoformat(),
    }
