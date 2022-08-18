"""Test User Module"""
from models import User


def test_new_user(app):  # pylint: disable=unused-argument
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the User is created correctly
    """
    user = User(
        name="Spider Man",
        email="some@email.com",
        senha="somepassword"
    )
    user.save()
