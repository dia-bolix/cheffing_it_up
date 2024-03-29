import os

import pymongo as pm

import pytest

import db.db_connect as dbc

RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)

TEST_DB = dbc.MENU_DB
TEST_COLLECT = 'test_collect'
# can be used for field and value:
TEST_NAME = 'test'


@pytest.fixture(scope='function')
def temp_rec():
    dbc.connect_db()
    dbc.client[TEST_DB][TEST_COLLECT].insert_one({TEST_NAME: TEST_NAME})
    # yield to our test function
    yield
    dbc.client[TEST_DB][TEST_COLLECT].delete_one({TEST_NAME: TEST_NAME})


def test_fetch_one(temp_rec):
    ret = dbc.fetch_one(TEST_COLLECT, {TEST_NAME: TEST_NAME})
    assert ret is not None


def test_fetch_one_not_there(temp_rec):
    ret = dbc.fetch_one(TEST_COLLECT, {TEST_NAME: 'not a field value in db!'})
    assert ret is None


def test_fetch_all(temp_rec):
    ret = dbc.fetch_all(TEST_COLLECT)
    assert isinstance(ret, list)
    assert len(ret) >= 1


def test_fetch_all_as_dict(temp_rec):
    ret = dbc.fetch_all_as_dict(TEST_NAME, TEST_COLLECT)
    assert isinstance(ret, dict)
    assert len(ret) >= 1
