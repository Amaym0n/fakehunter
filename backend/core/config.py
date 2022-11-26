import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE = 'JobBoard'
    PROJECT_VERSION = '0.1.0'

    # Database
    POSTGRES_USER = os.getenv(key='POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv(key='POSTGRES_PASSWORD')
    POSTGRES_SERVER = os.getenv(key='POSTGRES_SERVER', default='localhost')
    POSTGRES_PORT = os.getenv(key='POSTGRES_PORT', default='5432')
    POSTGRES_DB = os.getenv(key='POSTGRES_DB')
    POSTGRES_CONN_STRING = \
        f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'


settings = Settings()
