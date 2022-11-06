"""
This module encapsulates the details of the menu
"""


TEST_MENU = 'Test Menu'

NAME = 'Name'
MEAL_OF_DAY = 'Meal of Day'
INGREDIENTS = 'Ingredients'
CALORIES = 'Calories'
MACRONUTRIENTS = 'Macronutrients'
MICRONUTRIENTS = 'Micronutrients'
APIE = "Apple Pie"
PPIE = "Pumkin Pie"

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


def menu_exists(name):
    """
    Returns a true/false value given the name of a menu item.
    """
    return name in FOOD_MENU


def get_food():
    """
    Returns a list of all the current names of food available.
    """
    return list(FOOD_MENU.keys())


def get_food_details(name):
    """
    Given the name of a food, returns a dictonary with the nutritional details.
    """
    return FOOD_MENU.get(name, None)


def add_food(name, details):
    """
    Given the name of a food and a dictonary with it's nutritional values,
    will check if it's a vaild entry then add to the list of foods.
    """
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Requried {field=} missing from details')
    FOOD_MENU[name] = details


def get_food_by_ingredient(ingredient):
    """
    Given a name of an ingredient, returns a list of names with all the menu
    items that include that ingredient.
    """
    result = []
    for i in FOOD_MENU:
        if ingredient in FOOD_MENU[i][INGREDIENTS]:
            result.append(FOOD_MENU[i][NAME])
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


def main():
    food = get_food()
    print(f'{food=}')
    print(f'{get_food_details(TEST_MENU)=}')
    print(get_food_by_time_of_day("Dessert"))


if __name__ == '__main__':
    main()
