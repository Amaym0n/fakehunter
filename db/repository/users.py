from pydantic import EmailStr
from sqlalchemy.orm import Session

from core.hash_client import Hasher
from db import Users
from schemas.users_schema import UsersCreate


async def create_new_user(user: UsersCreate, db: Session) -> Users:
    user = Users(username=user.username, email=user.email,
                 hashed_password=Hasher.get_password_hash(plain_password=user.password),
                 is_active=True, is_superuser=False)
    db.add(instance=user)
    db.commit()
    db.refresh(instance=user)
    return user


async def retrieve_user(user_email: EmailStr, db: Session) -> Users:
    user = db.query(Users).filter(Users.email == user_email).first()
    return user


async def delete_user(user_id: int, db: Session) -> int:
    count_deleted_rows = db.query(Users).filter(Users.id == user_id).delete()
    db.commit()
    return count_deleted_rows


async def retrieve_user_password(user_email: EmailStr, db: Session) -> str:
    password = db.query(Users.hashed_password).filter(Users.email == user_email).one()[0]
    return password
