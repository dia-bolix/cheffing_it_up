import os
import bcrypt
import pymongo as pm

REMOTE = "1"
LOCAL = "0"

MENU_DB = 'food_menudb'
LOGIN_PW_COLLECTION = 'login_pw'

client = None

PASSWORD = 'password'
NAME = 'name'
EMAIL = 'email'
FULL_NAME = 'full_name'


def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)


def add_user(name, password, details,
             collection=LOGIN_PW_COLLECTION, db=MENU_DB):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')

    hashed_password = hash_password(password)
    details[PASSWORD] = hashed_password
    details[NAME] = name

    # Insert the user details into the MongoDB collection
    insert_one(collection, details, db=db)


def authenticate_user(name, password,
                      collection=LOGIN_PW_COLLECTION, db=MENU_DB):
    user_details = fetch_one(collection, {NAME: name}, db=db)

    if user_details is None:
        return False

    hashed_password = user_details[PASSWORD]
    return verify_password(password, hashed_password)


def connect_db():
    """
    This provides a uniform way to connect to the DB across all uses.
    Returns a mongo client object... maybe we shouldn't?
    Also set global client variable.
    We should probably either return a client OR set a
    client global.
    """
    global client
    if client is None:  # not connected yet!
        print("Setting client because it is None.")
        if os.environ.get("LOCAL_MONGO", LOCAL) == LOCAL:
            password = os.environ.get("MENU_MONGO_PW")
            if not password:
                raise ValueError('You must set your password '
                                 + 'to use Mongo in the cloud.')
            print("Connecting to Mongo in the cloud.")
            client = pm.MongoClient(f'mongodb+srv://cheffin:{password}'
                                    + '@cluster0.fcwlpnk.mongodb.net/'
                                    + '?retryWrites=true&w=majority')
        else:
            print("Connecting to Mongo locally.")
            client = pm.MongoClient()


def fetch_all(collection, db=MENU_DB):
    if client is None:
        connect_db()
    ret = []
    for doc in client[db][collection].find():
        ret.append(doc)
    return ret


def fetch_one(collection, filt, db=MENU_DB):
    """
    Find with a filter and return on the first doc found.
    """
    if client is None:
        connect_db()

    for doc in client[db][collection].find(filt):
        doc['_id'] = str(doc['_id'])
        return doc


def fetch_all_as_dict(key, collection, db=MENU_DB):
    ret = {}
    for doc in client[db][collection].find():
        del doc['_id']
        ret[doc[key]] = doc
    return ret


def insert_one(collection, doc, db=MENU_DB):
    """
    Insert a single doc into collection.
    """
    if client is None:
        connect_db()

    print(f'{db=}')
    return client[db][collection].insert_one(doc)


def del_one(collection, filt, db=MENU_DB):
    """
    Find with a filter and return on the first doc found.
    """
    result = client[db][collection].delete_one(filt)
    return result.deleted_count


def update_one(collection, query, update, db=MENU_DB):
    return client[db][collection].update_one(query, update)


def del_all(collection, db=MENU_DB):
    if client is None:
        connect_db()
    # return client[db].list_collection_names()
    result = client[db][collection].delete_many({})
    return result.deleted_count
