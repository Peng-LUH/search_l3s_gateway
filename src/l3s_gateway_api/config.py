import os
from pathlib import Path
from dotenv import load_dotenv
from pprint import pprint
load_dotenv(".env")

HERE = Path(__file__).parent
SQLITE_TEST = "sqlite:///" + str(HERE / "test.db")

# load db env variables
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")


POSTGRES_DATABASE_DEV = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# POSTGRES_DATABASE_DEV = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@pgsql:{POSTGRES_PORT}/{POSTGRES_DB}"
# POSTGRES_DATABASE_PROD = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@production-db:{POSTGRES_PORT}/{POSTGRES_DB}"
# POSTGRES_PROD = "sqlite:///" + str(HERE / "prod.db")

# SQLITE_DEV = os.getenv("DB_URL")
# SQLITE_TEST = os.getenv("DB_URL")
# SQLITE_PROD = os.getenv("DB_URL")

class Config:
    """Base Configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "open sesame")
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRE_HOURS = 0
    TOKEN_EXPIRE_MINUTES = 0
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SWAGGER_UI_DOC_EXPANSION = "list"
    RESTX_MASK_SWAGGER = False
    JSON_SORT_KEYS = False


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = SQLITE_TEST


class DevelopmentConfig(Config):
    """Development configuration."""

    TOKEN_EXPIRE_MINUTES = 15
    SQLALCHEMY_DATABASE_URI = POSTGRES_DATABASE_DEV


class ProductionConfig(Config):
    """Production configuration."""

    TOKEN_EXPIRE_HOURS = 1
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = POSTGRES_DATABASE_DEV
    PRESERVE_CONTEXT_ON_EXCEPTION = True


ENV_CONFIG_DICT = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)


def get_config(config_name):
    """Retrieve environment configuration settings."""
    pprint(config_name)
    pprint(ENV_CONFIG_DICT)
    print(list(ENV_CONFIG_DICT.keys()))
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)
