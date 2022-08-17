"""History Module"""
from app import app


@app.route("/history")
def history():
    return {"ok": "history"}
