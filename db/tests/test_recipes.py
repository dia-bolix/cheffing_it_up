import pytest

import db.recipes as fm

import os

from unittest import skip

RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)

TEST_DEL_NAME = 'Menu to be deleted'


def create_menu_details():
    details = {
        fm.NAME: 'test menu',
        fm.MEAL_OF_DAY: 'Dinner',
        fm.INGREDIENTS: ['dough', 'tomato sauce',
                         'cheese', 'pepperoni'],
        fm.CALORIES: 250,
        fm.MACRONUTRIENTS: {
            'Protein': 10,
            'Carbohydrates': 30,
            'Fat': 12
        },
        fm.MICRONUTRIENTS: {
            'Vitamin A': 0,
            'Vitamin C': 5,
            'Calcium': 200,
            'Iron': 1
        }
    }
    return details


@pytest.fixture(scope='function')
def temp_menu():
    # if not RUNNING_ON_CICD_SERVER:
    #     fm.add_food("test", {})
    #     yield
    #     return True
    #     # fm.del_game(gm.TEST_GAME_NAME)
    # else:
    #     yield
    #     return True
    fm.add_food(fm.TEST_MENU, create_menu_details())
    yield
    fm.delete_food(fm.TEST_MENU)

# TO BE ADDED
# def test_get_menu(temp_menu):
#     fms = fm.get_food()
#     assert isinstance(fms, list)
#     assert len(fms) > 0


def test_get_menu():
    if not RUNNING_ON_CICD_SERVER:
        fms = fm.get_food()
        assert isinstance(fms, list)
        assert len(fms) > 0


def test_get_food_by_time_of_day():
    result = fm.get_food_by_time_of_day("ANY TIME")
    assert isinstance(result, list)


def test_get_menu_dict():
    fms = fm.get_food_dict()
    assert isinstance(fms, dict)
    assert len(fms) > 0


def test_get_menu_details(temp_menu):
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
        fm.add_food('a new menu item', {'foo': 'bar'})


def test_get_food_by_ingredient(temp_menu):
    # Add a test food item with specific ingredients
    test_ingredients = ['dough', 'tomato sauce', 'cheese', 'pepperoni']
    test_food_details = create_menu_details()

    # Get food by ingredient
    fms = fm.get_food_by_ingredient(test_ingredients)
    print('fms is', fms)

    # Check that we got the right food
    assert len(fms) == 1
    assert fms[0] == test_food_details[fm.NAME]


def test_update_food_details(temp_menu):
    new_details = {
        fm.CALORIES: 300,
        fm.MEAL_OF_DAY: 'Lunch',
        fm.INGREDIENTS: ['test_ingredient']
    }
    fm.update_food_details(fm.TEST_MENU, new_details)
    updated_menu = fm.get_food_details(fm.TEST_MENU)

    assert updated_menu[fm.CALORIES] == new_details[fm.CALORIES]
    assert updated_menu[fm.MEAL_OF_DAY] == new_details[fm.MEAL_OF_DAY]
    assert updated_menu[fm.INGREDIENTS] == new_details[fm.INGREDIENTS]


def test_wrong_update_food_details(temp_menu):
    right_name = 'name'
    wrong_name = 123
    wrong_details = []
    right_details = {
        fm.CALORIES: 300,
        fm.MEAL_OF_DAY: 'Lunch',
        fm.INGREDIENTS: ['test_ingredient']
    }
    # testing name isn't of right type
    with pytest.raises(TypeError):
        fm.update_food_details(wrong_name, right_details)
    # testing that food_details isn't of right type
    with pytest.raises(TypeError):
        fm.update_food_details(right_name, wrong_details)


def test_get_food_by_calories_range(temp_menu):
    min_calories = 200
    max_calories = 300
    menus_in_range = fm.get_food_by_calories_range(min_calories, max_calories)

    for menu in menus_in_range:
        menu_details = fm.get_food_details(menu)
        assert min_calories <= menu_details[fm.CALORIES] <= max_calories


def test_get_food_by_meal_of_day(temp_menu):
    meal_of_day = 'ANY TIME'
    menus_by_meal_of_day = fm.get_food_by_meal_of_day(meal_of_day)

    for menu in menus_by_meal_of_day:
        menu_details = fm.get_food_details(menu)
        assert menu_details[fm.MEAL_OF_DAY].lower() == meal_of_day.lower()


@pytest.fixture(scope='function')
def new_menu():
    return fm.add_food(TEST_DEL_NAME, create_menu_details())


def test_del_menu(new_menu):
    fm.delete_food(TEST_DEL_NAME)
    assert not fm.menu_exists(TEST_DEL_NAME)


def test_add_menu():
    fm.add_food(fm.TEST_MENU, create_menu_details())
    assert fm.menu_exists(fm.TEST_MENU)
    fm.delete_food(fm.TEST_MENU)


@skip("adding a skip test")
def skip_test():
    return
