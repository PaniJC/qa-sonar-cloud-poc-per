from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.exceptions.exceptions import CredentialsException

def add_exception_handlers(app):
    @app.exception_handler(HTTPException)
    async def custom_http_exception_handler(request, exc):
        if exc.status_code == status.HTTP_401_UNAUTHORIZED:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "error": {
                        "status_code": status.HTTP_401_UNAUTHORIZED,
                        "type": "Credentials Exception",
                        "message": {
                            "unauthenticated": "Invalid credentials.",
                        },
                    }
                },
                headers={"WWW-Authenticate": "Bearer"},
            )
        return await app.exception_handler(exc)(request, exc)
    @app.exception_handler(CredentialsException)
    async def credentials_exception_handler(
        request: Request, exc: CredentialsException
    ):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error": {
                    "status_code": status.HTTP_401_UNAUTHORIZED,
                    "type": "Credentials Exception",
                    "message": {
                        "credentials": exc.message,
                    },
                }
            },
            headers={"WWW-Authenticate": "Bearer"},
        )