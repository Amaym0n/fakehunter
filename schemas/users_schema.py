from pydantic import BaseModel, EmailStr, constr


class UsersCreate(BaseModel):
    """ Schema that helps to validate data from create user route """
    username: constr(min_length=5)
    email: EmailStr
    password: constr(min_length=5)


class ShowUser(BaseModel):
    """ Schema for responses """
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

