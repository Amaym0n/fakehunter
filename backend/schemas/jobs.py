from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class JobBase(BaseModel):
    title: Optional[str] = None
    company_name: Optional[str] = None
    company_url: Optional[str] = None
    location: str = "Remote"
    description: Optional[str] = None
    date_posted: Optional[str] = datetime.now().date()


class JobCreate(JobBase):
    title: str
    company_name: str
    location: str
    description: str


class ShowJob(JobBase):
    title: str
    company_name: str
    company_url: Optional[str]
    description: str
    location: str
    date_posted: date

    class Config:
        orm_mode = True
