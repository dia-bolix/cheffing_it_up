import pytest

import db.users as usr


def test_get_users():
    usrs = usr.get_users()
    assert isinstance(usrs, list)


def test_get_user_details():
    test_user_name = "testuser"
    usr_dets = usr.get_user_details(test_user_name)
    assert isinstance(usr_dets, dict)


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        usr.add_user(7, "password", {usr.EMAIL: "test@example.com"})


def test_add_wrong_details_type():
    with pytest.raises(TypeError):
        usr.add_user('a new user', "password", [usr.EMAIL, "test@example.com"])


def test_add_missing_field():
    with pytest.raises(ValueError):
        usr.add_user('a new user', "password", {'foo': 'bar'})


def test_add_user():
    username = 'testuser'
    password = 'testpassword'
    details = {
        usr.EMAIL: 'test@example.com',
        usr.FULL_NAME: 'Test User',
    }
    if usr.user_exists(username):
        usr.delete_user(username)

    usr.add_user(username, password, details)
    assert usr.user_exists(username)
    assert usr.authenticate_user(username, password)
