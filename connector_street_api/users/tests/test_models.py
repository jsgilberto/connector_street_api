import pytest

from connector_street_api.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User):
    # assert user.get_absolute_url() == f"/users/{user.username}/"
    assert user.get_absolute_url() == True
