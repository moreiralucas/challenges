"""Home Module"""
from app import app


@app.route("/home")
def home():
    return {"ok": "home"}
