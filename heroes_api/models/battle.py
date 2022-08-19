"""Battle Model Module"""
from datetime import datetime
from .base import BaseModelMixin, db, fs_mixin


class Battle(db.Model, fs_mixin, BaseModelMixin):
    """Battle Model"""

    __tablename__ = "battle"

    begin = db.Column(db.DateTime)
    end = db.Column(db.DateTime)

    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=False)
    hero = db.relationship("Hero", backref=db.backref("heroes", lazy=True))

    threat_id = db.Column(db.Integer, db.ForeignKey("threat.id"), nullable=False)
    threat = db.relationship("Threat", backref=db.backref("threats", lazy=True))

    def __repr__(self):
        return f"<{self.threat} vs {self.hero}>"

    def start_battle(self):
        """Start the battles"""
        self.begin = datetime.utcnow()
        self.save()

    def finish_battle(self):
        """Finish the battles"""
        self.end = datetime.utcnow()
        self.save()
