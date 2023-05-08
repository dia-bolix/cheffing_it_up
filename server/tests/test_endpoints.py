
import pytest
from http import HTTPStatus

import server.endpoints as ep

import db.users as usr
import db.recipes as fm
import db.food_types as ft
import db.db_connect as dbc

from unittest.mock import patch

TEST_CLIENT = ep.app.test_client()
TEST_FOOD_TYPE = 'breakfast'
SAMPLE_FOOD_TYPE_LIST = ["breakfast", "lunch", "dinner"]


SAMPLE_USER_NM = 'SampleUser'
SAMPLE_USER_PW = 'StrongSamplePassword'
SAMPLE_USER_EMAIL = 'sample@gmail.com'
SAMPLE_USER_FULL_NAME = 'SampleFullName'

SAMPLE_USER = {
    usr.NAME: SAMPLE_USER_NM,
    usr.EMAIL: 'x@y.com',
    usr.FULL_NAME: 'Sample User',
}


def test_hello():
    """
    See if Hello works.
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()

    assert isinstance(resp_json[ep.MESSAGE], str)


@patch("db.food_types.get_food_types", return_value=SAMPLE_FOOD_TYPE_LIST)
def test_get_food_type_list(mock_get_food_type_list):
    """
    See if we can get a food type list properly.
    Return should look like:
        {FOOD_TYPE_LIST_NM: [list of food types...]}
    """
    resp_json = TEST_CLIENT.get(f'food_types/list')
    assert resp_json.status_code == HTTPStatus.OK
    assert isinstance(resp_json.json, dict)
    assert isinstance(resp_json.json[ep.FOOD_TYPE_LIST_NM], list)


# def test_get_food_type_list():
#     """
#     See if we can get a charcter type list properly.
#     Return should look like:
#         {CHAR_TYPE_LIST_NM: [list of chars types...]}
#     """
#     resp_json = TEST_CLIENT.get(ep.FOOD_TYPE_LIST_W_NS).get_json()
#     assert isinstance(resp_json[ep.FOOD_TYPE_LIST_NM], list)


def test_get_food_type_list_not_empty():
    """
    See if we can get a charcter type list properly.
    Return should look like:
        {CHAR_TYPE_LIST_NM: [list of chars types...]}
    """
    resp_json = TEST_CLIENT.get(ep.FOOD_TYPE_LIST_W_NS).get_json()
    assert len(resp_json[ep.FOOD_TYPE_LIST_NM]) > 0


# def test_get_food_type_details():
#     """
#     testing testing
#     """
#     resp_json = TEST_CLIENT.get(f'{ep.FOOD_TYPE_DETAILS}/{TEST_FOOD_TYPE}').get_json()
#     assert TEST_FOOD_TYPE in resp_json
#     assert isinstance(resp_json[TEST_FOOD_TYPE], dict)


# def test_get_food_type_details():
#     """
#     testing testing
#     """
#     resp = TEST_CLIENT.get(f'{ep.FOOD_TYPE_DETAILS}/{TEST_FOOD_TYPE}')
#     resp_json = resp.get_json()
#     if resp_json is not None:
#         assert TEST_FOOD_TYPE in resp_json
#         assert isinstance(resp_json[TEST_FOOD_TYPE], dict)
#     else:
#         assert False, 'Response is None'


# def test_add_user(app, client):
#     # Call the /register endpoint to add the sample user
#     response = client.post('/users/register', json={
#         'username': SAMPLE_USER_NM,
#         'password': SAMPLE_USER_PW,
#         'email': SAMPLE_USER_EMAIL,
#         'full_name': SAMPLE_USER_FULL_NAME
#     })

#     # Check if the user has been added successfully
#     assert response.status_code == 201

#     # Check if the user exists
#     assert usr.user_exists(SAMPLE_USER_NM)



def test_get_user_list():
    """
    See if we can get a user list properly.
    Return should look like:
        {USER_LIST_NM: [list of users types...]}
    """
    dbc.connect_db()
    resp = TEST_CLIENT.get(ep.USER_LIST_W_NS)
    resp_json = resp.get_json()
    print(resp_json)  # Add this line to inspect the response
    assert isinstance(resp_json[ep.USER_LIST_NM], list)

