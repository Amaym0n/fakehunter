from passlib.context import CryptContext

pwt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hasher:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """ Verify plain_password and hashed_password """
        return pwt_context.verify(secret=plain_password, hash=hashed_password)

    @staticmethod
    def get_password_hash(plain_password: str) -> str:
        """ Hash plain_password """
        return pwt_context.hash(secret=plain_password)
