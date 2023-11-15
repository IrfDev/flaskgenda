from dotenv import load_dotenv, get_key

load_dotenv(dotenv_path=".env")


def get_env_key(env_key: str) -> str | None:
    """Function to get the environment value based on the key"""
    return get_key(key_to_get=env_key, dotenv_path=".env")


class Config:
    SECRET_KEY = get_env_key("SECRET_KEY")
    JWT_ALGORITHM = get_env_key("JWT_ALGORITHM")
    DB_NAME = get_env_key("DATABASE_NAME")
    DB_HOST = get_env_key("DATABASE_HOST")
    DB_USER = get_env_key("DATABASE_USER")
    DB_PASSWORD = get_env_key("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    )
