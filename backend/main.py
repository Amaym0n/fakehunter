from fastapi import FastAPI

from core.config import settings
from db import Base
from db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return app


App = start_application()


@App.get(path='/hello')
def hello_api():
    return {'detail': 'Hello World'}
