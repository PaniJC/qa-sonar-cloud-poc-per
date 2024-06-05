from fastapi import FastAPI
from ddtrace import patch, tracer
from routers.routers import routers
from exceptions.exception_handler import add_exception_handlers


patch(fastapi=True)

tracer.configure(
    hostname="datadog-agent",
    port=8126,
)

app = FastAPI()

add_exception_handlers(app)

app.include_router(routers)
