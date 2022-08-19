"""Test Home Page Module"""
import json


def test_home_page(app):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200
    res = json.loads(response.data.decode('utf-8'))
    assert isinstance(res, dict)
    assert "ok" in res
    assert res["ok"] == "index"
