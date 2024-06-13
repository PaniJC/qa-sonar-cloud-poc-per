import os

from app.services.groups_service import get_groups, search_user_groups


def test_get_groups():
    groups = get_groups()
    assert type(groups) == dict
    assert type(groups["groups"]) == list


def test_search_user_groups():
    user_email = os.environ("USER_EMAIL")
    groups = search_user_groups(user_email)
    assert type(groups) == dict
    assert type(groups["groups"]) == list
