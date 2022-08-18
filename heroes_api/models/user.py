"""User Model Module"""
from .base import BaseModel, db, fs_mixin


class User(db.Model, fs_mixin, BaseModel):
    """User Model"""

    __tablename__ = "user"

    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(256))

    def __repr__(self):
        return f"<Name {self.name}>"
