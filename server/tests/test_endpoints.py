
import pytest

import server.endpoints as ep

import db.users as usr
from unittest.mock import patch

TEST_CLIENT = ep.app.test_client()
TEST_FOOD_TYPE = 'breakfast'
SAMPLE_FOOD_TYPE_LIST = ["breakfast", "lunch", "dinner"]


SAMPLE_USER_NM = 'SampleUser'
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


@patch("db.users.get_food_type_list", return_value=SAMPLE_FOOD_TYPE_LIST)
def test_get_food_type_list(mock_get_food_type_list):
    """
    See if we can get a food type list properly.
    Return should look like:
        {FOOD_TYPE_LIST_NM: [list of food types...]}
    """
    resp_json = TEST_CLIENT.get(ep.FOOD_TYPE_LIST_W_NS).get_json()
    assert isinstance(resp_json[ep.FOOD_TYPE_LIST_NM], list)


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


def test_add_user():
    """
    Test adding a user.
    """
    resp = TEST_CLIENT.post(ep.USER_ADD, json=SAMPLE_USER)
    print(usr.users)
    assert usr.user_exists(SAMPLE_USER_NM)
    usr.del_user(SAMPLE_USER_NM)


def test_get_user_list():
    """
    See if we can get a user list properly.
    Return should look like:
        {USER_LIST_NM: [list of users types...]}
    """
    resp = TEST_CLIENT.get(ep.USER_LIST_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.USER_LIST_NM], list)
