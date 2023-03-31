from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base


class Users(Base):
    """ Model for Jobs table """
    id = Column(type_=Integer, primary_key=True, index=True)
    username = Column(type_=String, unique=True, nullable=False)
    email = Column(type_=String, unique=True, nullable=False, index=True)
    hashed_password = Column(type_=String, nullable=False)
    is_active = Column(type_=Boolean(), default=True)
    is_superuser = Column(type_=Boolean(), default=False)
    jobs = relationship('Jobs', back_populates='owner')
