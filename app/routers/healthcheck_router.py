from fastapi import APIRouter

healthcheck_router = APIRouter()


@healthcheck_router.get("/")
async def healthcheck():
    """
    Endpoint for healthcheck.

    Returns:
        dict: A dictionary with the status "ok".
    """
    return {"status": "ok"}
