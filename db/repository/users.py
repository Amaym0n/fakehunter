from pydantic import EmailStr
from sqlalchemy.orm import Session

from core.hash_client import Hasher
from db import User
from schemas.users_schema import UsersCreate


async def create_new_user(user: UsersCreate, db: Session) -> User:
    user = User(username=user.username, email=user.email,
                hashed_password=Hasher.get_password_hash(plain_password=user.password),
                is_active=True, is_superuser=False)
    db.add(instance=user)
    db.commit()
    db.refresh(instance=user)
    return user


async def retrieve_user(user_email: EmailStr, db: Session) -> User:
    user = db.query(User).filter(User.email == user_email).first()
    return user


async def delete_user(user_id: int, db: Session) -> int:
    count_deleted_rows = db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return count_deleted_rows


async def retrieve_user_password(user_email: EmailStr, db: Session) -> str:
    password = db.query(User.hashed_password).filter(User.email == user_email).one()[0]
    return password
