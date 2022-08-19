"""Hero Model Module"""
from typing import Dict

from .base import BaseModelMixin, db, fs_mixin


class Hero(db.Model, fs_mixin, BaseModelMixin):
    """Hero Model"""

    HEROES_CLASS: Dict = {"S": 3, "A": 2, "B": 1, "C": 0}

    __tablename__ = "hero"
    name = db.Column(db.String(128), nullable=False)
    class_name = db.Column(db.String(128), nullable=False)
    class_number = db.Column(db.Integer)
    last_battle = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Name {self.name}>"

    def __fs_after_commit__(self, create: bool = False):
        if self.class_number is None or self.class_number == "":
            self.class_number = self.HEROES_CLASS[self.class_name]
            self.save()
