from typing import Union

from passlib.context import CryptContext

pwt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hasher:
    """ Class to hash user passwords and verify it """

    @staticmethod
    def verify_password(plain_password: Union[str, bytes], hashed_password: Union[str, bytes]) -> bool:
        return pwt_context.verify(secret=plain_password, hash=hashed_password)

    @staticmethod
    def get_password_hash(plain_password: Union[str, bytes]) -> str:
        return pwt_context.hash(secret=plain_password)
