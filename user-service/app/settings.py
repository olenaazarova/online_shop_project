import os


class Settings:
    database_url = os.getenv("DATABASE_URL", "")
    auth_service_url = os.getenv("AUTH_SERVICE_URL", "http://api-gateway")
    internal_api_key = os.getenv("INTERNAL_API_KEY", "local-internal-key")


settings = Settings()
