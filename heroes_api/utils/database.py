"""Database Utils Module"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import ENVIRONMENT


def init_database(app: Flask, database: SQLAlchemy):
    """Create all models of database"""
    if ENVIRONMENT != "test":
        with app.app_context():
            database.create_all()
