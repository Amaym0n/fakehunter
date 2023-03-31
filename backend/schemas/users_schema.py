from pydantic import BaseModel, EmailStr


class UsersCreate(BaseModel):
    """ Schema that helps to validate data from create user route """
    username: str
    email: EmailStr
    password: str


class ShowUser(UsersCreate):
    """ Schema for responses """
    id: int
