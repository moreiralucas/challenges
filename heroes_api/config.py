"""Config Module"""
import os

from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("DB_HOST")
port = os.environ.get("DB_PORT")
user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
database = os.environ.get("POSTGRES_DB")
ENVIRONMENT= os.environ.get("ENVIRONMENT", 'dev')

SECRET_KEY = "GRJikjauHy4gZQKp7usrkucTEP2VEwzJ"
SQLALCHEMY_DATABASE_URI = f"postgresql://{user}:{password}@{host}:{port}/{database}"


class Config(object):
    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Settings
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    ENVIRONMENT='dev'
    # FLASK_APP="app"

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    DEBUG = True
    TESTING = True
    ENVIRONMENT='test'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    DEBUG = False
    TESTING = False
    ENVIRONMENT='prod'
