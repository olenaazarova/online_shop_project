from pydantic import BaseModel, EmailStr, Field


class CreateProfileRequest(BaseModel):
    auth_user_id: str
    email: EmailStr
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    phone: str | None = None


class UpdateProfileRequest(BaseModel):
    first_name: str | None = Field(default=None, min_length=1)
    last_name: str | None = Field(default=None, min_length=1)
    phone: str | None = None
