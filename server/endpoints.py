"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus
from flask import Flask
from flask_restx import Resource, Api, fields
import werkzeug.exceptions as wz
# import db.db as db

import db.food_types as ftyp

app = Flask(__name__)
api = Api(app)

LIST = 'list'
DETAILS = 'details'
HELLO = '/hello'
MESSAGE = 'message'
MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'
CHAR_TYPES_NS = 'character_types'
CHAR_TYPE_LIST = f'/{CHAR_TYPES_NS}/{LIST}'
CHAR_TYPE_LIST_NM = 'character_types_list'


A_CHAR_TYPE = 'Wizard'
ANOTHER_CHAR_TYPE = 'Warrior'


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


@api.route(CHAR_TYPE_LIST)
class CharacterTypeList(Resource):
    """
    This will get a list of character types.
    """
    def get(self):
        """
        Returns a list of character types.
        """
        return {CHAR_TYPE_LIST_NM: [A_CHAR_TYPE, ANOTHER_CHAR_TYPE]}


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
