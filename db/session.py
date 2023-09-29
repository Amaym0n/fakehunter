from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings


def get_db() -> Generator:
    try:
        db = Session()
        yield db
    finally:
        db.close()


engine = create_engine(url=settings.POSTGRES_DSN)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
