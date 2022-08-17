"""Base Models Module"""

from datetime import datetime
from flask_serialize import FlaskSerialize

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
fs_mixin = FlaskSerialize(db)


class BaseModel:  # (db.Model, fs_mixin):
    """Base Model Class"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # created = db.Column(db.DateTime, default=datetime.utcnow)
    # updated = db.Column(db.DateTime, default=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    # @classmethod
    # def delete(cls):
    #     is_successful = User.query.filter_by(username=_username).delete()
    #     db.session.commit()
    #     return bool(is_successful)
