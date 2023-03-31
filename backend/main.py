from fastapi import FastAPI
from starlette.responses import RedirectResponse

from core.config import settings
from db import Base, engine


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


def start_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get(path='/', response_class=RedirectResponse)
def redirecting():
    return 'docs'
