from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session

from db import get_db, Users
from db.repository.users import create_new_user, retrieve_user, delete_user
from schemas.users_schema import UsersCreate, ShowUser

users_router = APIRouter()


@users_router.post(path='/user/', response_model=ShowUser, status_code=HTTPStatus.CREATED)
async def create_user(user: UsersCreate, db: Session = Depends(dependency=get_db)) -> Users:
    return await create_new_user(user=user, db=db)


@users_router.get(path='/user/{user_email}', response_model=ShowUser, status_code=HTTPStatus.OK)
async def retrieve_user_by_email(user_email: EmailStr, db: Session = Depends(dependency=get_db)) -> Users:
    retrieved_user = await retrieve_user(user_email=user_email, db=db)
    if retrieved_user is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f'User with email {user_email} does not exist')


@users_router.delete(path='/user/{user_id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_user_by_id(user_id: int, db: Session = Depends(dependency=get_db)) -> None:
    count_deleted_rows = await delete_user(user_id=user_id, db=db)
    if count_deleted_rows == 0:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f"User with id {user_id} does not exist")
