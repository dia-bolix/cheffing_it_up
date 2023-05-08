import db.db_connect as dbc


NAME = 'name'
EMAIL = 'email'
FULL_NAME = 'full_name'

REQUIRED_FLDS = [EMAIL]


def user_exists(name):
    dbc.connect_db()
    """
    Returns whether or not a user exists.
    """
    return dbc.fetch_one(dbc.LOGIN_PW_COLLECTION,
                         {NAME: name}) is not None


def add_user(name, password, details):
    dbc.connect_db()
    missing_fields = [field for field in REQUIRED_FLDS if field not in details]
    if missing_fields:
        raise ValueError(f'Required fields {missing_fields} \
                        are missing from details.')

    dbc.add_user(name, password, details)


def authenticate_user(name, password):
    dbc.connect_db()
    return dbc.authenticate_user(name, password)


def get_users():
    dbc.connect_db()
    users = dbc.fetch_all(dbc.LOGIN_PW_COLLECTION)
    return [user[NAME] for user in users]


def get_user_details(user):
    dbc.connect_db()
    return dbc.fetch_one(dbc.LOGIN_PW_COLLECTION, {NAME: user})


def del_user(name):
    dbc.connect_db()
    dbc.del_one(dbc.LOGIN_PW_COLLECTION, {NAME: name})


def delete_user(username):
    dbc.connect_db()
    """Deletes a user from the database."""
    dbc.del_one(dbc.LOGIN_PW_COLLECTION, {NAME: username})


def main():
    dbc.connect_db()
    users = get_users()
    print(f'{users=}')
    print(f'{get_user_details("Test user")=}')


if __name__ == '__main__':
    main()
