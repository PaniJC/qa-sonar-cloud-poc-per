from fastapi import FastAPI

from app.routers.routers import routers
from app.exceptions.exception_handler import add_exception_handlers

app = FastAPI()

add_exception_handlers(app)

app.include_router(routers)
