"""Threat Model Module"""
from .base import BaseModel, fs_mixin, db


class Threat(db.Model, fs_mixin, BaseModel):
    """Threat Model"""

    __tablename__ = "threat"

    danger_level = db.Column(db.String(128))
    monster_name = db.Column(db.String(128))
    location = db.Column(db.String(256))
    danger_level_number = db.Column(db.Integer)

    def __repr__(self):
        return "<Name %r>" % self.monster_name
