"""User Module"""
from app import app
from models import User


@app.route("/user/<int:user_id>", methods=["GET", "PUT", "DELETE"])
@app.route("/user", methods=["GET", "POST"])
def user(user_id=None):
    """User View"""
    return User.fs_get_delete_put_post(user_id)
