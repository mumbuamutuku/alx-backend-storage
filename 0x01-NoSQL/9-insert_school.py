#!/usr/bin/env python3
"""
a Python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """ Function to insert a new document
    Return the new _id
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
