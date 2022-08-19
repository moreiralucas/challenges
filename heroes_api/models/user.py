"""User Model Module"""
from flask_bcrypt import generate_password_hash
from .base import BaseModelMixin, db, fs_mixin


class User(db.Model, fs_mixin, BaseModelMixin):
    """User Model"""

    __tablename__ = "user"

    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(256))
    __fs_update_fields__ = ["name", "email"]
    __fs_exclude_json_serialize_fields__ = ["password"]

    def __repr__(self):
        return f"<Name {self.name}>"

    def set_password(self, password: str, save: bool = True):
        """Generate password hash"""
        self.password = generate_password_hash(password)
        if save:
            self.save()
