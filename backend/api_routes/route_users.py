from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db, Users
from db.repository.users import create_new_user
from schemas.users_schema import UsersCreate, ShowUser

users_router = APIRouter()


@users_router.post(path='/users', response_model=ShowUser)
def create_user(user: UsersCreate, db: Session = Depends(dependency=get_db)) -> Users:
    created_user = create_new_user(user=user, db=db)
    return created_user
