from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Jobs(Base):
    """ Model for Jobs table """
    id = Column(type_=Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(type_=String, nullable=False)
    company_name = Column(type_=String, nullable=False)
    company_url = Column(type_=String, nullable=False)
    location = Column(type_=String, nullable=False)
    description = Column(type_=String, nullable=False)
    date_posted = Column(type_=Date)
    is_active = Column(type_=Boolean(), default=True)
    owner_id = Column(ForeignKey('user_id'), type_=Integer)
    owner = relationship('Users', back_populates='jobs')
