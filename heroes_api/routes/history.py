"""History Module"""
from app import app
from models import Battle

@app.route("/history", methods=["GET"])
def history():
    """History View"""
    return Battle.fs_get_delete_put_post()
