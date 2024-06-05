from fastapi import APIRouter, Depends

from routers.healthcheck_router import healthcheck_router
from routers.groups_router import groups_router
from middelwares.verify_auth import verify_auth

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
