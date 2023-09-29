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
