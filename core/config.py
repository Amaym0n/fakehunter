from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_TITLE: str = 'FAKEHUNTER'
    PROJECT_VERSION: str = '0.1.1'

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_DSN: str


settings = Settings()
