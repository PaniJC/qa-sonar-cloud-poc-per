from fastapi import APIRouter, Depends
from typing import Annotated
from services.groups_service import search_user_groups
from middelwares.verify_auth import verify_auth


groups_router = APIRouter()


@groups_router.get("/")
def groups(json: Annotated[dict, Depends(verify_auth)]):
    """
    Endpoint to get the groups from the Google Workspace Admin SDK.

    Returns:
        dict: A dictionary with the groups.
    """
    return search_user_groups(json["email"])
