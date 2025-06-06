#!/usr/bin/env python3
'''Python script that provides some stats
about Nginx logs stored in MongoDB'''
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    logs_count = collection.count_documents({})
    print("{} logs".format(logs_count))
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        number = collection.count_documents({'method': method})
        print("\tmethod {}: {}".format(method, number))
    status_check_count = collection.count_documents({'method': 'GET',
                                                      'path': '/status'})
    print("{} status check".format(status_check_count))
