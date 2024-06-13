from typing import Annotated
from fastapi import APIRouter, Depends

from middelwares.verify_auth import verify_auth
from services.user_service import get_user_service
from services.search import searchFiles

user_router = APIRouter()

@user_router.get("/")
def get_user():
    return get_user_service()

@user_router.get("/files/{token}")
def get_files(token: str):
    return searchFiles(token)