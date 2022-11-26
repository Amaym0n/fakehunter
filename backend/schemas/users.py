from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """ Pydantic class to check user data """

    username: str
    password: str
    email: EmailStr
