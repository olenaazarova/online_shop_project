import psycopg
from fastapi import HTTPException

from app import repository
from app.schemas import CreateProfileRequest, UpdateProfileRequest


def create_user_profile(payload: CreateProfileRequest) -> dict:
    try:
        return repository.create_profile(payload.model_dump())
    except psycopg.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="User profile already exists")


def get_user_profile(auth_user_id: str) -> dict:
    profile = repository.find_by_auth_user_id(auth_user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    return profile


def change_user_profile(auth_user_id: str, payload: UpdateProfileRequest) -> dict:
    profile = repository.update_profile(auth_user_id, payload.model_dump(exclude_unset=True))
    if not profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    return profile
