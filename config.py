from pydantic import BaseSettings


class Configuration(BaseSettings):
    db_name: str
    db_password: str
    DATABASE_URL = 'sqlite:///SQl/home/khushal/school_management.db'

    class Config:
        env_file = '.env'
