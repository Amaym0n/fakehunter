from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.models.users import Users
from schemas.users import UserCreate


class UserMethods:
    """ Class with methods to update/delete/create users """

    @staticmethod
    def create_new_user(user: UserCreate, db: Session):
        user = Users(username=user.username, email=user.email,
                     hashed_password=Hasher.get_password_hash(plain_password=user.password), is_active=True,
                     is_superuser=False)
        db.add(instance=user)
        db.commit()
        db.refresh(instance=user)
        return user
