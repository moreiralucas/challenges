"""Index Module"""
from app import app


@app.route("/")
def index():
    """Index View"""
    return {"ok": "index"}
