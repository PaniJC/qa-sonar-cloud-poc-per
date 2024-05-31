from fastapi import APIRouter, Depends

from app.routers.healthcheck_router import healthcheck_router
from app.routers.groups_router import groups_router
from app.middelwares.verify_auth import verify_auth

routers = APIRouter()

routers.include_router(
    healthcheck_router,
    prefix="",
    tags=["healthcheck"],
)

routers.include_router(
    groups_router,
    prefix="/groups",
    tags=["groups"],
    dependencies=[Depends(verify_auth)],
)
