import os

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig, ProductionConfig, TestingConfig, ENVIRONMENT

# App Factory
def create_app(db: SQLAlchemy):
    app = Flask(__name__)

    if ENVIRONMENT == "prod":
        config_class = ProductionConfig
    elif ENVIRONMENT == "test":
        config_class = TestingConfig
    else:
        config_class = DevelopmentConfig

    app.config.from_object(config_class)
    db.init_app(app)

    return app
