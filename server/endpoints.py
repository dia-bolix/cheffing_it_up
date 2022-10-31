"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus

from flask import Flask, request
from flask_restx import Resource, Api, fields
import werkzeug.exceptions as wz
# import db.db as db

import db.food_types as ftyp
import db.food_menu as fm

app = Flask(__name__)
api = Api(app)

LIST = 'list'
DETAILS = 'details'
HELLO = '/hello'
MESSAGE = 'message'
ADD = 'add'
FIND = 'find'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'

FOOD_TYPES_NS = 'food_types'
FOOD_TYPE_LIST = f'/{FOOD_TYPES_NS}/{LIST}'
FOOD_TYPE_LIST_NM = f'{FOOD_TYPES_NS}_list'
FOOD_TYPE_DETAILS = f'/{FOOD_TYPES_NS}/{DETAILS}'

FOOD_MENU_NS = 'food_menu'
FOOD_MENU_LIST = f'/{FOOD_MENU_NS}/{LIST}'
FOOD_MENU_LIST_NM = f'{FOOD_MENU_NS}_list'
FOOD_MENU_DETAILS = f'/{FOOD_MENU_NS}/{DETAILS}'
FOOD_MENU_ADD = f'/{FOOD_MENU_NS}/{ADD}'
FOOD_MENU_FIND = f'/{FOOD_MENU_NS}/{FIND}'


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
        Gets the main recipe menu.
        """
        return {MAIN_MENU_NM: {'the': 'menu'}}


@api.route(FOOD_TYPE_LIST)
class FoodTypeList(Resource):
    """
    This will get a list of character types.
    """
    def get(self):
        """
        Returns a list of character types.
        """
        return {FOOD_TYPE_LIST_NM: ftyp.get_food_types()}


@api.route(f'{FOOD_TYPE_DETAILS}/<food_types>')
class FoodTypeDetails(Resource):
    """
    This will return details on a character type.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, food_types):
        """
        This will return details on a character type.
        """
        ct = ftyp.get_food_types_details(food_types)
        if ct is not None:
            return {food_types: ftyp.get_food_types_details(food_types)}
        else:
            raise wz.NotFound(f'{food_types} not found.')


@api.route(FOOD_MENU_LIST)
class MenuList(Resource):
    """
    This will get a list of current menu
    """
    def get(self):
        """
        Returns a list of current menus
        """
        return {FOOD_MENU_LIST_NM: fm.get_food()}


@api.route(f'{FOOD_MENU_DETAILS}/<food_types>')
class MenuDetails(Resource):
    """
    this will return details on menu
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, food_menu):
        """
        Return a list of menu types
        """
        mt = fm.get_food_details(food_menu)
        if mt is not None:
            return {food_menu: fm.get_food_details(food_menu)}
        else:
            raise wz.NotFound(f'{food_menu} not found.')


menu_fields = api.model('NewMenu', {
    fm.NAME: fields.String,
    fm.MEAL_OF_DAY: fields.String,
    fm.INGREDIENTS: fields.String,
    fm.CALORIES: fields.Integer,
    fm.MACRONUTRIENTS: fields.String,
    fm.MICRONUTRIENTS: fields.String
})


@api.route(FOOD_MENU_ADD)
class AddMenu(Resource):
    """
    Add a Menu item
    """
    @api.expect(menu_fields)
    def post(self):
        """
        Add a Menu item
        """
        print(f'{request.json=}')
        name = request.json[fm.NAME]
        fm.add_food(name, request.json)
        del request.json[fm.NAME]


@api.route(FOOD_MENU_FIND)
class FindMenu(Resource):
    """
    Find a menu from given ingredient
    """
    @api.expect(fields.String)
    def post(self):
        """
        Find menu item rom ingredident
        """
        print(f'{request.json=}')
        mt = fm.get_food_by_ingredient(request.json)
        if mt is not None:
            return {"Dish": fm.get_food_by_ingredient(request.json)}
        else:
            raise wz.NotFound(f'{request.json} not found')


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
