"""Hero Model Module"""
from typing import Dict
from .base import BaseModel, fs_mixin, db


class Hero(db.Model, fs_mixin, BaseModel):
    """Hero Model"""

    HEROES_CLASS = {"S": 3, "A": 2, "B": 1, "C": 0}

    __tablename__ = "hero"
    name = db.Column(db.String(128))
    class_name = db.Column(db.String(128))
    class_number = db.Column(db.Integer)

    def __repr__(self):
        return "<Name %r>" % self.name

    def save(self):
        if self.class_number is None:
            self.class_number = self.HEROES_CLASS[self.class_name.upper()]
        return super().save()

    def __fs_before_update__(self, data_dict: Dict):
        data: Dict = dict(data_dict)
        data['class_number'] = self.HEROES_CLASS[data.get('class_name')]
        return data
