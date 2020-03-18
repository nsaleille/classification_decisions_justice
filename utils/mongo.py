import pandas as pd
from pymongo import MongoClient

def _connect_mongo(db, host, port, username = None, password = None):
    """ A util for making a connection to mongo """

    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        port = int(float(port))
        conn = MongoClient(host, port)

    return conn[db]

def read_mongo(db, collection, query={}, no_id=False, pandas = False):
    """ Read from Mongo and Store into DataFrame """
    cursor = db[collection].find(query)
    collection = db[collection]

    if pandas:
        df =  pd.DataFrame(list(cursor))
        if no_id:
            del df['_id']
        return df
    else:
        return collection
