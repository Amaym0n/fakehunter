from pydantic import BaseModel, EmailStr


class UsersCreate(BaseModel):
    """ Schema that helps to validate data from create user route """
    username: str
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    """ Schema for responses """
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

