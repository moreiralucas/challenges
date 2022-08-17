"""Hero Module"""
from app import app
from models import Hero


@app.route("/hero/<int:hero_id>", methods=["GET", "PUT", "DELETE"])
@app.route("/hero", methods=["GET", "POST"])
def hero(hero_id=None):
    """Hero View"""
    return Hero.fs_get_delete_put_post(hero_id)
