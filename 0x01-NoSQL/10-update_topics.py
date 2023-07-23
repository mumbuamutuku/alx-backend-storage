#!/usr/bin/env python3
"""
Python function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    function to change all topics
    mongo_collection will be the pymongo collection object
    name (string) will be the school name to update
    topics(list of strings) will be the list of topics approached in the school
    """
    filter = {"name": name}

    update = {"$set": {"topics": topics}}

    res = mongo_collection.update_many(filter, update)

    return res.modified_count > 0
