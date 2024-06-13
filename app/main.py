from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ddtrace.runtime import RuntimeMetrics
from ddtrace import patch
from routers.routers import routers
from exceptions.exception_handler import add_exception_handlers

patch(logging=True)
RuntimeMetrics.enable()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_exception_handlers(app)

app.include_router(routers)
