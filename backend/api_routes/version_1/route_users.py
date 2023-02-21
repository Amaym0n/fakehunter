from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.repository.users import create_new_user, change_user_to_inactive
from db.session import get_db
from schemas.users import UserCreate, ShowUser

router = APIRouter()


@router.post(path='/user', response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(dependency=get_db)):
    user = create_new_user(user=user, db=db)
    return user


@router.delete(path='/user{user_id}')
def delete_user(user_id: int, db: Session = Depends(dependency=get_db)):
    return change_user_to_inactive(user_id=user_id, db=db)
