#!/usr/bin/env python3
'''Function schools_by_topic'''


def schools_by_topic(mongo_collection, topic):
    '''function that returns the list of
    school having a specific topic'''
    return mongo_collection.find({'topic': topic})
