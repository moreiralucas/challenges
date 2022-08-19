"""Threat Model Module"""
from typing import Dict
from sqlalchemy.dialects.postgresql import JSON
from .base import BaseModelMixin, db, fs_mixin


class Threat(db.Model, fs_mixin, BaseModelMixin):
    """Threat Model"""

    THREAT_LEVEL: Dict = {
        "God": 3,
        "Dragon": 2,
        "Tiger": 1,
        "Wolf": 0,
    }

    __tablename__ = "threat"

    danger_level = db.Column(db.String(128), nullable=False)
    monster_name = db.Column(db.String(128), nullable=False)
    location = db.Column(JSON, nullable=False)
    danger_level_number = db.Column(db.Integer)

    def __repr__(self):
        return f"<Name {self.monster_name}>"

    def save(self):
        if self.danger_level_number is None:
            self.danger_level_number = self.THREAT_LEVEL[self.danger_level]
        return super().save()

    def __fs_before_update__(self, data_dict: Dict):
        data: Dict = dict(data_dict)
        assert data["danger_level"] in self.THREAT_LEVEL
        data["danger_level_number"] = self.THREAT_LEVEL[data.get("danger_level")]
        return data

    @classmethod
    def from_json(cls, data: Dict):
        """Create a Threat instance from a json data"""
        return cls(
            danger_level=data["dangerLevel"],
            monster_name=data["monsterName"],
            location=data["location"][0],
        )
