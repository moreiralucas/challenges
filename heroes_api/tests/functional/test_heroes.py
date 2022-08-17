"""Test Home Page Module"""
import json
from typing import Dict, List

from flask.testing import FlaskClient
from werkzeug.test import TestResponse

from models import Hero


def test_list_heroes(app):
    """
    GIVEN an list heroes configured
    WHEN the '/hero' is required (GET)
    THEN list all heroes in database
    """
    for i in range(3):
        hero: Hero = Hero(
            name=f"Thor_{i}",
            class_name="A",
        )
        hero.save()

    client = app.test_client()
    url = '/hero'

    response: TestResponse = client.get(url)
    assert response.status_code == 200
    res: List = json.loads(response.data.decode('utf-8'))
    assert isinstance(res, list)
    assert len(res) == 3

def test_get_hero(app):
    """
    GIVEN an hero id
    WHEN the '/hero/id' is required (GET)
    THEN return the hero data
    """
    hero: Hero = Hero(
        name="Spider Man",
        class_name="B",
    )
    hero.save()
    hero_id: int = hero.id

    client: FlaskClient = app.test_client()
    url = f'/hero/{hero_id}'

    response: TestResponse = client.get(url)
    assert response.status_code == 200

def test_update_hero(app):
    """
    GIVEN an hero object
    WHEN the '/hero/id' is request (PUT)
    THEN update the hero object and return updated data
    """
    hero: Hero = Hero(
        name="Doctor Strange",
        class_name="S",
    )
    hero.save()
    hero_id: int = hero.id
    data: Dict = {
        "name": "Iron man",
        "class_name": "A"
    }

    client: FlaskClient = app.test_client()
    url = f'/hero/{hero_id}'

    response: TestResponse = client.put(url, data=json.dumps(data))
    assert response.status_code == 200
    res: Dict = json.loads(response.data.decode('utf-8'))
    assert isinstance(res["item"], dict)
    assert res["item"]["name"] == "Iron man"
    assert res["item"]["class_name"] == "A"
    assert res["item"]["class_number"] == 2
    assert res["message"] == "Updated"
