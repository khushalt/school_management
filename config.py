from pydantic import BaseSettings


class Configuration(BaseSettings):
    db_name: str
    db_password: str
    DATABASE_URL = str

    class Config:
        env_file = '.env'
