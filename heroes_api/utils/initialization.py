"""Initialization Module"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import ENVIRONMENT, DevelopmentConfig, ProductionConfig, TestingConfig


def create_app(data_base: SQLAlchemy):
    """App Factory"""
    app: Flask = Flask(__name__)

    if ENVIRONMENT == "prod":
        config_class = ProductionConfig
    elif ENVIRONMENT == "test":
        config_class = TestingConfig
    else:
        config_class = DevelopmentConfig

    app.config.from_object(config_class)
    data_base.init_app(app)

    return app
