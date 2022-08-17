"""Auth Module"""
from app import app


@app.route("/auth/login", methods=["POST"])
def login():
    """Handle authentication"""
    return {"ok": "login"}


@app.route("/auth/logout", methods=["GET"])
def logout():
    """Handle logout"""
    return {"ok": "logout"}
