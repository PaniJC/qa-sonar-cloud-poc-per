from fastapi import APIRouter
from ddtrace import tracer

healthcheck_router = APIRouter()

@tracer.wrap()
@healthcheck_router.get("/")
async def healthcheck():
    """
    Endpoint for healthcheck.

    Returns:
        dict: A dictionary with the status "ok".
    """
    return {"status": "ok"}
