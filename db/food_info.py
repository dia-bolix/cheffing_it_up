"""
This module encapsulates details about the food.
WILL DELETE
"""

listOfFoods = ["Apple Pie", "Pumpkin Pie", "Blueberry Muffin"]
FOOD_INFO = {"APPLE PIE": {'Calories': 67, 'Vitamins': ["A", "C"],
             'Ingredients': ["Apples", "wheat flour", "oil", "cream",
                             "sugar"]},
             "PUMPKIN PIE": {'Calories': 323, 'Vitamins': ["B6"],
                             'Ingredients': ["Pumpkin flour", "butter", "egg",
                                             "cornstarch", "cinnamon",
                                             "nutmeg", "salt", "milk", "cream"
                                             ]},
             "BLUEBERRY MUFFIN": {'Calories': 467, 'Vitamins': ["A", "C"],
                                  'Ingredients': ["flour", "blueberry",
                                                  "salt", "baking power",
                                                  "oil", "egg",
                                                  "vanilla extract", "sugar",
                                                  "milk"]}}
FOOD_INFO_TEST = {"FOOD": {'Calories': 100, 'Vitamins': ["A", "B", "C", "D"],
                  'Ingredients': ["Water"]}}


def get_food_info():
    return list(FOOD_INFO.keys())


def get_food_info_details(food):
    return FOOD_INFO[food]


def main():
    char_types = get_food_info()
    print(char_types)


if __name__ == '__main__':
    main()
