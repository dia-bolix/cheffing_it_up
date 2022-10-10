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

REQUIRED_FLDS = [NAME, MEAL_OF_DAY, INGREDIENTS,
                 CALORIES, MACRONUTRIENTS, MICRONUTRIENTS]
food = {TEST_MENU: {NAME: 'CAKE',
                    MEAL_OF_DAY: 'ANY TIME',
                    INGREDIENTS: "MAGIC, SUGAR",
                    CALORIES: 10,
                    MACRONUTRIENTS: "Fats: 1g, Carbs: 1g, Protein: 10g",
                    MICRONUTRIENTS: "Vitamin A: 100%, Vitamin C: 100%, Iron: 100%"},
        'Apple Pie': {NAME: "APPLE PIE",
                    MEAL_OF_DAY: "Dessert",
                    INGREDIENTS: "Apples, Wheat flour, oil, cream,sugar",
                    CALORIES: 237,
                    MACRONUTRIENTS: "Carbs: 43g, Protein: 2.4g, Fats: 14g",
                    MICRONUTRIENTS: "Vitamin A: 3.1%, Vitamin C: 6.7%, Calcium: 1.1%, Iron: 3.1%"},
        'Pumpkin Pie': {NAME: "PUMPKIN PIE",
                    MEAL_OF_DAY: "Dessert",
                    INGREDIENTS: "Pumpkin flour, butter, egg, cornstarch, cinnamon, nutmeg, salt, milk, cream",
                    CALORIES: 323,
                    MACRONUTRIENTS: "Fats: 13g, Carbs: 46g, Protein: 52.g",
                    MICRONUTRIENTS: "Vitamin A: 91%, Calcium: 6.5%, Iron: 6.7%"},
             }


def menu_exists(name):
    return name in food


def get_food():
    return list(food.keys())


def get_food_details(name):
    return food.get(name, None)


def add_food(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Requried {field=} missing from details')
    food[name] = details


def main():
    food = get_food()
    print(f'{food=}')
    print(f'{get_food_details(TEST_MENU)=}')


if __name__ == '__main__':
    main()