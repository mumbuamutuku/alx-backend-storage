#!/usr/bin/env python3
"""0. Writing strings to Redis """

import redis
import uuid
from typing import Union


class Cache:
    """
    Create a Cache class
    """
    def __init__(self):
        """
        __init__ method - store an instance of the Redis client
        _redis - private variable
        using redis.Redis()
        flush the instance using flushdb
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """"
        a store method that takes a data argument and returns a string
        should generate a random key (e.g. using uuid),
        store the input data in Redis using the random key
        return the key
        data can be a str, bytes, int or float.
        """
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int]:
        """
        a get method that take a key string argument
        an optional Callable argument named fn
        This callable will be used to convert the data
        back to the desired format.
        """
        value = self.__redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        paremetize str with correct conversion function
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        parametize int with correct conversion function
        """
        return self.get(key, fn=int)
