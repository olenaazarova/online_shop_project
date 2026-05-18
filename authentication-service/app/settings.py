import os


class Settings:
    database_url = os.getenv("DATABASE_URL", "")
    redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
    redis_sentinels = os.getenv("REDIS_SENTINELS", "")
    redis_master_name = os.getenv("REDIS_MASTER_NAME", "auth-redis")
    jwt_secret = os.getenv("JWT_SECRET", "local-development-secret")
    jwt_ttl_seconds = int(os.getenv("JWT_TTL_SECONDS", "7200"))
    user_service_url = os.getenv("USER_SERVICE_URL", "http://user-service:8000")
    internal_api_key = os.getenv("INTERNAL_API_KEY", "local-internal-key")


settings = Settings()
