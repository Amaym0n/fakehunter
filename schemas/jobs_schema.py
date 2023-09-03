from pydantic import BaseModel, AnyUrl
from pydantic.types import date, constr


class JobCreate(BaseModel):
    """ Schema that helps to validate data from create user route """
    title: constr(min_length=5)
    description: constr(min_length=10)
    company_name: str
    company_url: AnyUrl
    location: str
    date_posted: date
