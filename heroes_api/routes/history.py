"""History Module"""
from app import app


@app.route("/history")
def history():
    """History View"""
    return {"ok": "history"}
