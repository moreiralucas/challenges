"""Test Threat Module"""
from models import Threat


def test_new_threat(app):  # pylint: disable=unused-argument
    """
    GIVEN
    WHEN
    THEN
    """
    threat = Threat(
        danger_level="Wolf",
        monster_name="The Lone Butcher Dragon",
        location={
            "lat": 53.318813068796395,
            "lng": -2.2234260979885097
        },
    )
    threat.save()
    assert threat.danger_level_number == 0

    threat = Threat.from_json({
        "location": [
            {
                "lat": -23.546735992658377,
                "lng": -46.933910011724585
            }
        ],
        "dangerLevel": "God",
        "monsterName": "Blazeteeth"
    })
    threat.save()
    assert threat.danger_level_number == 3
    assert threat.monster_name == "Blazeteeth"
