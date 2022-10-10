
"""
This is a module to detail our food types
"""

BREAKFAST = 'breakfast'
LUNCH = 'lunch'
DINNER = 'dinner'

FOOD_TYPES = {BREAKFAST: {'time': "6am - 8am"},
              LUNCH: {'time': "11am-1pm"},
              DINNER: {'time': "5pm-7pm"}, }


def get_food_types():
    return list(FOOD_TYPES.keys())


def get_food_types_details(food_type):
    return FOOD_TYPES.get(food_type, None)


def main():
    food_types = get_food_types()
    print(food_types)


if __name__ == '__main__':
    main()
    