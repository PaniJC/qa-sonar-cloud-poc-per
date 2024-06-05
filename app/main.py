from fastapi import FastAPI
from ddtrace.runtime import RuntimeMetrics
from routers.routers import routers
from exceptions.exception_handler import add_exception_handlers


RuntimeMetrics.enable()

app = FastAPI()

add_exception_handlers(app)

app.include_router(routers)
