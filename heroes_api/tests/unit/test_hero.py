from models import Hero


def test_new_hero(app):
    """
    GIVEN a Hero model
    WHEN a new Hero is created
    THEN check the class number is defined correctly
    """
    hero = Hero(
        name="Spider Man",
        class_name="B",
    )
    hero.save()
    assert hero.class_number == 1
