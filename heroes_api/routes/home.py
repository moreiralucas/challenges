"""Home Module"""
from app import app


@app.route("/home")
def home():
    """Home View"""
    return {"ok": "home"}
