from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from core.hash_client import Hasher
from db.repository.users import retrieve_user, retrieve_user_password
from db.session import Session, get_db
from schemas.users_schema import UserLogin

token_router = APIRouter(tags=['JWT'])


class Token(BaseModel):
    access_token: str
    token_type: str


@token_router.post(path='/token', response_model=Token)
async def login_for_access_token(user_login: UserLogin, db: Session = Depends(dependency=get_db)) -> Token:
    """ Get JWT token """
    retrieved_user = await retrieve_user(user_email=user_login.email, db=db)
    if not retrieved_user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f"There is no user with this email")
    hashed_user_password = await retrieve_user_password(user_email=user_login.email, db=db)
    verify_password = Hasher().verify_password(plain_password=user_login.password,
                                               hashed_password=hashed_user_password)
    if not verify_password:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,
                            detail=f"Incorrect password")
