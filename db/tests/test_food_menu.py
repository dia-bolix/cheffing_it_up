# from lib2to3.pytree import type_repr
# from msilib.schema import Error
import pytest

import db.food_menu as fm

import os

RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)


def test_get_menu():
    if not RUNNING_ON_CICD_SERVER:
        fms = fm.get_food()
        assert isinstance(fms, list)
        assert len(fms) > 1


def test_get_menu_dict():
    if not RUNNING_ON_CICD_SERVER:
        fmd = fm.get_food_dict()
        assert isinstance(fmd[fm.TEST_MENU], dict)
        assert len(fmd[fm.TEST_MENU]) > 1


def test_get_menu_details():
    fm_details = fm.get_food_details(fm.TEST_MENU)
    assert isinstance(fm_details, dict)


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        fm.add_food(7, {})


def test_add_wrong_details_type():
    with pytest.raises(TypeError):
        fm.add_food('a new menu item', [])


def test_add_missing_field():
    with pytest.raises(ValueError):
        fm.add_food('a new menu item', {'foo':'bar'})


def test_get_food_by_ingredient():
    fm_result = fm.get_food_by_ingredient(fm.TEST_MENU)
    assert isinstance(fm_result, list)


def test_get_food_by_time_of_day():
    result = fm.get_food_by_time_of_day(fm.TEST_MENU)
    assert isinstance(result, list)


def test_add_menu():
    if not RUNNING_ON_CICD_SERVER:
        details = {}
        for field in fm.REQUIRED_FLDS:
            details[field] = 2
        fm.add_food(fm.TEST_MENU, details)
        #assert fm.menu_exists(fm.TEST_MENU)
