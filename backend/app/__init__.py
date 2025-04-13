from fastapi import FastAPI
from .routers import note


def create_app() -> FastAPI:
    app = FastAPI(title="BiliNote")
    app.include_router(note.router, prefix="/api")
    return app
