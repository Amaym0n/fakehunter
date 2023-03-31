from pydantic import BaseModel
from pydantic.types import date


class JobsCreate(BaseModel):
    """ Schema that helps to validate data from create user route """
    title: str
    company_name: str
    location: str
    date_posted: date
