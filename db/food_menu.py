"""
This module encapsulates the details of the menu
"""

import db.db_connect as dbc

TEST_MENU = 'test menu'

NAME = 'name'
MEAL_OF_DAY = 'meal of Day'
INGREDIENTS = 'ingredients'
CALORIES = 'calories'
MACRONUTRIENTS = 'Macronutrients'
MICRONUTRIENTS = 'Micronutrients'
APIE = "apple pie"
PPIE = "pumpkin pie"

REQUIRED_FLDS = [NAME, MEAL_OF_DAY, INGREDIENTS,
                 CALORIES, MACRONUTRIENTS, MICRONUTRIENTS]
FOOD_MENU = {TEST_MENU: {NAME: 'CAKE',
                         MEAL_OF_DAY: 'ANY TIME',
                         INGREDIENTS: "MAGIC, SUGAR",
                         CALORIES: 10,
                         MACRONUTRIENTS: "Fats: 1g, Carbs: 1g, Protein: 10g",
                         MICRONUTRIENTS: "Vitamin A: 100%, Vitamin C: 100%"},
             APIE: {NAME: "APPLE PIE",
                    MEAL_OF_DAY: "Dessert",
                    INGREDIENTS: "Apples, Wheat flour,oil,cream,sugar",
                    CALORIES: 237,
                    MACRONUTRIENTS: "Carbs:43g,Protein:2.4g,Fats: 14g",
                    MICRONUTRIENTS: """Vitamin A: 3.1%,Vitamin C: 6.7%,
                                        Calcium: 1.1%, Iron: 3.1%"""},
             PPIE: {NAME: "PUMPKIN PIE",
                    MEAL_OF_DAY: "Dessert",
                    INGREDIENTS: """Pumpkin flour, butter, egg, cornstarch,
                                    cinnamon, nutmeg, salt, milk, cream""",
                    CALORIES: 323,
                    MACRONUTRIENTS: "Fats: 13g, Carbs: 46g, Protein: 52.g",
                    MICRONUTRIENTS: """Vitamin A: 91%, Calcium: 6.5%,
                                        Iron: 6.7%"""},
             }


MENU_KEY = 'name'
MENU_COLLECT = 'FOOD_MENU'


def menu_exists(name):
    """
    Returns a true/false value given the name of a menu item.
    """
    return name in FOOD_MENU


def get_food():
    """
    Returns a list of all the current names of food available.
    """
    dbc.connect_db()
    return dbc.fetch_all(MENU_COLLECT)
    # return list(FOOD_MENU.keys())


def get_food_dict():
    """
    Returns a dictonarys of all the current names of food available.
    """
    dbc.connect_db()
    return dbc.fetch_all_as_dict(MENU_KEY, MENU_COLLECT)
    # return FOOD_MENU


# def get_food_details(name):
#     """
#     Given the name of a food, returns a dictonary with
#     the nutritional details.
#     """
#     return FOOD_MENU.get(name.lower(), None)


def get_food_details(name):
    """
    Given the name of a food, returns a dictonary with the nutritional details.
    """
    dbc.connect_db()
    return dbc.fetch_one(MENU_COLLECT, {MENU_KEY: name})


def add_food(name, details):
    """
    Given the name of a food and a dictonary with it's nutritional values,
    will check if it's a vaild entry then add to the list of foods.
    """
    doc = details
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Requried {field=} missing from details')

    FOOD_MENU[name.lower()] = details

    dbc.connect_db()
    doc[MENU_KEY] = name
    return dbc.insert_one(MENU_COLLECT, doc)


def get_food_by_ingredient(ingredient):
    """
    Given a name of an ingredient, returns a list of names with all the menu
    items that include that ingredient.
    """
    if not isinstance(ingredient, list):
        raise ValueError("The argument must be a list of ingredients.")
    fd = get_food_dict()
    result = []
    for i in fd:
        if ingredient in fd[i][INGREDIENTS]:
            result.append(fd[i][NAME])
    return result


def get_food_by_time_of_day(time_of_day):
    """
    Given the type of meal (breakfast, lunch, dinner), return a list of names
    for all of the meals served during that time of day.
    """
    result = []
    for i in FOOD_MENU:
        if time_of_day in FOOD_MENU[i][MEAL_OF_DAY]:
            result.append(FOOD_MENU[i][NAME])
    return result


def del_menu(name):
    """
    Given the name of a menu, delete that menu from the database.
    """
    return dbc.del_one(MENU_COLLECT, {MENU_KEY: name})


def main():
    food = get_food()
    print(f'{food=}')
    #     print(f'{get_food_details(TEST_MENU)=}')
    #     print(get_food_by_time_of_day("Dessert"))
    #     print(get_food_by_ingredient("cheese"))


if __name__ == '__main__':
    main()
