import os

import pymongo as pm

REMOTE = "0"
LOCAL = "1"

MENU_DB = 'food_menudb'

client = None


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
            print("Connecting to Mongo locally.")
            client = pm.MongoClient()


def fetch_all(collection, db=MENU_DB):
    print('in here')
    print(client[db][collection])
    ret = []
    for doc in client[db][collection].find():
        ret.append(doc)
    return ret


def fetch_one(collection, filt, db=MENU_DB):
    """
    Find with a filter and return on the first doc found.
    """
    for doc in client[db][collection].find(filt):
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
    client[db][collection].insert_one(doc)
