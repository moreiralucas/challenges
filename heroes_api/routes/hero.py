"""Hero Module"""
from models import Hero
from app import app


@app.route("/hero/<int:hero_id>", methods=["GET", "PUT", "DELETE"])
@app.route("/hero", methods=["GET", "POST"])
def hero(hero_id=None):
    return Hero.fs_get_delete_put_post(hero_id)
