#!/usr/bin/env python3
'''Function insert_school'''


def insert_school(mongo_collection, **kwargs):
    ''' function that inserts a new docE ument in a
    collection based on kwargs'''
    ids = mongo_collection.insert_one(kwargs)
    return ids.inserted_id
