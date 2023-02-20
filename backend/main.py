from fastapi import FastAPI

from api_routes import api_router
from core.config import settings
from db import Base
from db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app: FastAPI):
    app.include_router(router=api_router)


def start_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app=app)
    return app


App = start_application()
