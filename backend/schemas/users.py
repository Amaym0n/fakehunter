from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """ Pydantic class to check user data """

    username: str
    password: str
    email: EmailStr


class ShowUser(BaseModel):
    """ Response for create_user root """
    id: int
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
