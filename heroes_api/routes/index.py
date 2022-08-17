"""Index Module"""
from app import app


@app.route("/")
def index():
    return {"ok": "index"}
