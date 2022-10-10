
import pytest
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()
TEST_FOOD_TYPE = 'Breakfast'

def test_hello():
    """
    See if Hello works.
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)


def test_get_food_type_list():
    """
    See if we can get a charcter type list properly.
    Return should look like:
        {CHAR_TYPE_LIST_NM: [list of chars types...]}
    """
    resp_json = TEST_CLIENT.get(ep.FOOD_TYPE_LIST).get_json()
    assert isinstance(resp_json[ep.FOOD_TYPE_LIST_NM], list)


def test_get_food_type_list_not_empty():
    """
    See if we can get a charcter type list properly.
    Return should look like:
        {CHAR_TYPE_LIST_NM: [list of chars types...]}
    """
    resp_json = TEST_CLIENT.get(ep.FOOD_TYPE_LIST).get_json()
    assert len(resp_json[ep.FOOD_TYPE_LIST_NM]) > 0


def test_getfood_type_details():
    """
    testing testing
    """
    resp_json = TEST_CLIENT.get(f'{ep.FOOD_TYPE_DETAILS}/{TEST_FOOD_TYPE}').get_json()
    assert TEST_FOOD_TYPE in resp_json
    assert isinstance(resp_json[TEST_FOOD_TYPE], dict)

