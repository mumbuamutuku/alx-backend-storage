#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    script
    """
    connection_string = "mongodb://localhost:27017/"
    database_name = "logs"
    collection_name = "nginx"
    """Create a MongoClient"""
    client = MongoClient(connection_string)
    """Access the database and collection"""
    db = client[database_name]
    collection = db[collection_name]
    """Get the total number of documents in the collection"""
    total_logs = collection.count_documents({})
    """Get the number of documents for each HTTP method"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = [collection.count_documents(
        {"method": method}) for method in methods]
    """Get the number of documents with method=GET and path=/status"""
    status_logs = collection.count_documents(
            {"method": "GET", "path": "/status"})
    """Display the statistics"""
    print(f"Total logs: {total_logs}")
    print("Methods:")
    for method, count in zip(methods, method_stats):
        print(f"\tmethod {method}: {count}")
    print(f"{status_logs} status check")


if __name__ == "__main__":
    log_stats()
