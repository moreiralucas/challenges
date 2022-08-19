"""Start Flsk Module"""
# pylint: disable=unused-import,wrong-import-position
from flask_bcrypt import Bcrypt
from flask import Flask
from models.base import db
from utils import create_app, init_database
from services.listener import socket_heroes
from config import ENVIRONMENT

app: Flask = create_app(db)
init_database(app, db)
# bcrypt = Bcrypt(app)

if ENVIRONMENT != 'test':
    socket_heroes.start_socketio_connection(app)

import routes.auth
import routes.hero
import routes.history
import routes.home
import routes.index
import routes.user

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
