from fastapi import FastAPI

from routers.routers import routers
from exceptions.exception_handler import add_exception_handlers

app = FastAPI()

add_exception_handlers(app)

app.include_router(routers)
