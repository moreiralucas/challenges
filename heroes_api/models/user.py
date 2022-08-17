"""User Model Module"""
from .base import BaseModel, fs_mixin, db


class User(db.Model, fs_mixin, BaseModel):
    """User Model"""

    __tablename__ = "user"

    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    senha = db.Column(db.String(256))

    def __repr__(self):
        return "<Name %r>" % self.name
