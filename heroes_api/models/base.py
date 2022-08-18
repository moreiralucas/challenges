"""Base Models Module"""

from flask_serialize import FlaskSerialize
from flask_sqlalchemy import SQLAlchemy


db: SQLAlchemy = SQLAlchemy()
fs_mixin = FlaskSerialize(db)  # pylint: disable=invalid-name


class BaseModel:
    """Base Model Class"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # created = db.Column(db.DateTime, default=datetime.utcnow)
    # updated = db.Column(db.DateTime, default=datetime.utcnow)

    def save(self):
        """Save model data in database"""
        db.session.add(self)
        db.session.commit()

    # @classmethod
    # def delete(cls):
    #     is_successful = User.query.filter_by(username=_username).delete()
    #     db.session.commit()
    #     return bool(is_successful)
