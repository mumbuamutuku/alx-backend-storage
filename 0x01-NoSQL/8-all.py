#!/usr/bin/env python3
"""
function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    lists all documents
    Return an empty list if no document in the collection
    """
    all_doc = []

    item = mongo_collection.find()

    for doc in item:
        all_doc.append(doc)

    return all_doc
