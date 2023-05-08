import db.db_connect as dbc


NAME = 'name'
EMAIL = 'email'
FULL_NAME = 'full_name'

REQUIRED_FLDS = [EMAIL]


def user_exists(name):
    """
    Returns whether or not a user exists.
    """
    return dbc.fetch_one(dbc.LOGIN_PW_COLLECTION,
                         {NAME: name}) is not None


def add_user(name, password, details):
    missing_fields = [field for field in REQUIRED_FLDS if field not in details]
    if missing_fields:
        raise ValueError(f'Required fields {missing_fields} \
                        are missing from details.')

    dbc.add_user(name, password, details)


def authenticate_user(name, password):
    return dbc.authenticate_user(name, password)


def get_users():
    users = dbc.fetch_all(dbc.LOGIN_PW_COLLECTION)
    return [user[NAME] for user in users]


def get_user_details(user):
    return dbc.fetch_one(dbc.LOGIN_PW_COLLECTION, {NAME: user})


def del_user(name):
    dbc.del_one(dbc.LOGIN_PW_COLLECTION, {NAME: name})


def delete_user(username):
    """Deletes a user from the database."""
    dbc.del_one(dbc.LOGIN_PW_COLLECTION, {NAME: username})


def main():
    users = get_users()
    print(f'{users=}')
    print(f'{get_user_details("Test user")=}')


if __name__ == '__main__':
    main()
