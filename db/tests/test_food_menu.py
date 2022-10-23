# from lib2to3.pytree import type_repr
# from msilib.schema import Error
import pytest

import db.food_menu as fm


def test_get_menu():
    fms = fm.get_food()
    assert isinstance(fms, list)
    assert len(fms) > 1


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


def test_add_menu():
    details = {}
    for field in fm.REQUIRED_FLDS:
        details[field] = 2
    fm.add_food(fm.TEST_MENU, details)
    assert fm.menu_exists(fm.TEST_MENU)