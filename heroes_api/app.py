"""Start Flsk Module"""
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from utils import create_app
from models.base import db
 

# db = SQLAlchemy()
app = create_app(db)

# bcrypt = Bcrypt(app)
import routes.auth
import routes.hero
import routes.history
import routes.home
import routes.index


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")



"""
import os

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from project.config import DevelopmentConfig, ProductionConfig

db = SQLAlchemy()

# App Factory
def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    if "ZAPPA" in os.environ and os.environ["ZAPPA"] == "True":
        config_class = ProductionConfig
    app.config.from_object(config_class)

    with app.app_context():
        db.init_app(app)
        register_blueprints(app)

    @app.route("/", methods=["POST", "GET"])
    def root():
        return redirect(url_for("main.index"))

    return app
"""