"""Start Flsk Module"""
# pylint: disable=unused-import,wrong-import-position
from flask import Flask
from flask_bcrypt import Bcrypt

from models.base import db
from utils import create_app, init_database

app = create_app(db)
init_database(app, db)
# bcrypt = Bcrypt(app)

import routes.auth
import routes.hero
import routes.history
import routes.home
import routes.index

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
