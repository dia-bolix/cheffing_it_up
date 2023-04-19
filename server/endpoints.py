"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus

from flask import Flask, request
from flask_restx import Resource, Api, fields, Namespace
import werkzeug.exceptions as wz
from flask_cors import CORS

# import db.db as db


import db.food_types as ftyp
import db.recipes as fm
import db.users as usr

app = Flask(__name__)
api = Api(app)
cors = CORS(app)


RECIPES_NS = 'recipes'
USERS_NS = 'users'
FOOD_TYPES_NS = 'food_types'

users = Namespace(USERS_NS, 'Users')
api.add_namespace(users)
food_types = Namespace(FOOD_TYPES_NS, 'Food_Types')
api.add_namespace(food_types)
recipes = Namespace(RECIPES_NS, 'Recipes')
api.add_namespace(recipes)


LIST = 'list'
DICT = 'dict'
DETAILS = 'details'
HELLO = '/hello'
MESSAGE = 'message'
ADD = 'add'
FIND = 'find'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
USERS_NS = 'users'

FOOD_TYPE_LIST = f'/{LIST}'
FOOD_TYPE_DICT = f'/{DICT}'
FOOD_TYPE_DICT_W_NS = f'{FOOD_TYPES_NS}/{DICT}'
FOOD_TYPE_DICT_NM = f'{FOOD_TYPES_NS}_dict'
FOOD_TYPE_LIST_W_NS = f'{FOOD_TYPES_NS}/{LIST}'
FOOD_TYPE_LIST_NM = f'{FOOD_TYPES_NS}_list'
FOOD_TYPE_DETAILS = f'/{DETAILS}'

RECIPES_LIST = f'/{LIST}'
RECIPES_DICT = f'/{DICT}'
RECIPES_DICT_W_NS = f'{RECIPES_NS}/{DICT}'
RECIPES_DICT_NM = f'{RECIPES_NS}_dict'
RECIPES_LIST_W_NS = f'{RECIPES_NS}/{LIST}'
RECIPES_LIST_NM = f'{RECIPES_NS}_list'
RECIPES_DETAILS = f'/{DETAILS}'
RECIPES_ADD = f'/{ADD}'
RECIPES_FIND = f'/{FIND}'

USER_DICT = f'/{DICT}'
USER_DICT_W_NS = f'{USERS_NS}/{DICT}'
USER_DICT_NM = f'{USERS_NS}_dict'
USER_LIST = f'/{LIST}'

USER_LIST_W_NS = f'{USERS_NS}/{LIST}'
USER_LIST_NM = f'{USERS_NS}_list'
USER_DETAILS = f'/{USERS_NS}/{DETAILS}'
USER_ADD = f'/{ADD}'


@api.route(HELLO)
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """

    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {MESSAGE: 'hello world'}


@api.route(MAIN_MENU)
class MainMenu(Resource):
    """
    This will deliver our main menu.
    """

    def get(self):
        """
        Gets the main food menu.
        """
        return {'Title': MAIN_MENU_NM,
                'Default': 2,
                'Choices': {
                    '1': {'url': f'/{FOOD_TYPE_DICT_W_NS}', 'method': 'get',
                          'text': 'List Food Types'},
                    '2': {'url': f'/{RECIPES_DICT_W_NS}',
                          'method': 'get', 'text': 'List Recipes'},
                    '3': {'url': f'/{USER_DICT_W_NS}',
                          'method': 'get', 'text': 'List Users'},
                    'X': {'text': 'Exit'},
                }}


@food_types.route(FOOD_TYPE_LIST)
class FoodTypeList(Resource):
    """
    This will get a list of current food types.
    """

    def get(self):
        """
        Returns a list of current food types.
        """
        return {FOOD_TYPE_LIST_NM: ftyp.get_food_types()}


@food_types.route(FOOD_TYPE_DICT)
class FoodTypeDict(Resource):
    """
    This will get a dict of current food types
    """

    def get(self):
        """
        Returns a dict of current food types
        """
        return {'Data': ftyp.get_food_types_dict(),
                'Type': 'Data',
                'Title': 'Dictonary of recipes'}


@recipes.route(FOOD_TYPE_DICT)
class RecipeList(Resource):
    """
    This will get a dict of all the recipes currently in the database
    """

    def get(self):
        """
        This will get a dict of all the recipes currently in the database
        """
        return {'Data': fm.get_food_dict(),
                'Type': 'Data',
                'Title': 'Dictonary of recipes'}


@food_types.route(f'{FOOD_TYPE_DETAILS}/<food_types>')
class FoodTypeDetails(Resource):
    """
    This will return details about the types of food
    (breakfast, lunch, dinner)
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, food_types):
        """
        This will return details about the types of food
        (breakfast, lunch, dinner).
        """
        ct = ftyp.get_food_types_details(food_types)
        if ct is not None:
            return {food_types: ftyp.get_food_types_details(food_types)}
        else:
            return {}


@recipes.route(f'{RECIPES_DETAILS}/<name>')
class RecipeDetails(Resource):
    """
    This will return details on a recipe given its name
    """
    @recipes.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, name):
        """
        This will return details on a recipe given its name
        """
        mt = fm.get_food_details(name)
        if mt is not None:
            return {name: fm.get_food_details(name)}
        else:
            raise wz.NotFound(f'{name} not found.')


MACRONUTRIENTS = {}
MACRONUTRIENTS['Protein'] = fields.Integer(0)
MACRONUTRIENTS['Carbohydrates'] = fields.Integer(0)
MACRONUTRIENTS['Fat'] = fields.Integer(0)
MACRONUTRIENTS_payload = api.model('MACRONUTRIENTS', MACRONUTRIENTS)


MICRONUTRIENTS = {}
MICRONUTRIENTS['Vitamin A'] = fields.Integer(0)
MICRONUTRIENTS['Vitamin C'] = fields.Integer(0)
MICRONUTRIENTS['Calcium'] = fields.Integer(0)
MICRONUTRIENTS['Iron'] = fields.Integer(0)
MICRONUTRIENTS_payload = api.model('MICRONUTRIENTS', MICRONUTRIENTS)

recipe_fields = api.model('NewRecipe', {
    fm.NAME: fields.String,
    fm.MEAL_OF_DAY: fields.String,
    fm.INGREDIENTS: fields.List(fields.String),
    fm.CALORIES: fields.Integer,
    fm.MACRONUTRIENTS: fields.Nested(MACRONUTRIENTS_payload),
    fm.MICRONUTRIENTS: fields.Nested(MICRONUTRIENTS_payload)
})


@recipes.route(RECIPES_ADD)
class AddRecipe(Resource):
    """
    Add a recipe
    """
    @api.expect(recipe_fields)
    def post(self):
        """
        Add a recipe
        """
        print(f'{request.json=}')
        name = request.json[fm.NAME]
        fm.add_food(name, request.json)
        del request.json[fm.NAME]


@recipes.route(f'{RECIPES_FIND}/<ingredient>')
class FindRecipe(Resource):
    """
    Returns a list of names of recipes with given ingredient
    """
    @api.expect(fields.String)
    def get(self, ingredient):
        """
        Returns a list of names of recipes with given ingredient
        """
        mt = fm.get_food_by_ingredient(ingredient)
        if mt is not None:
            return {"Dishes with " + ingredient:
                    fm.get_food_by_ingredient(ingredient)}
        else:
            raise wz.NotFound(f'{request.json} not found')


@users.route(USER_DICT)
class UserDict(Resource):
    """
    This will get a list of currrent users.
    """

    def get(self):
        """
        Returns a list of current users.
        """
        return {'Data': usr.get_users_dict(),
                'Type': 'Data',
                'Title': 'Active Users'}


@users.route(USER_LIST)
class UserList(Resource):
    """
    This will get a list of currrent users.
    """

    def get(self):
        """
        Returns a list of current users.
        """
        return {USER_LIST_NM: usr.get_users()}


user_fields = api.model('NewUser', {
    usr.NAME: fields.String,
    usr.EMAIL: fields.String,
    usr.FULL_NAME: fields.String,
})


@api.route(USER_ADD)
class AddUser(Resource):
    """
    Add a user.
    """
    @api.expect(user_fields)
    def post(self):
        """
        Add a user.
        """
        print(f'{request.json=}')
        name = request.json[usr.NAME]
        del request.json[usr.NAME]
        usr.add_user(name, request.json)


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """

    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = ''
        # sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}
