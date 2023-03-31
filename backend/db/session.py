from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

engine = create_engine(url=settings.DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
