#!/usr/bin/env python3
"""
implement a get_page function (prototype: def get_page(url: str) -> str:).
"""

import requests
import redis
from functools import wraps

# Redis instance for caching
cache_redis = redis.Redis()


def track_url_access(func):
    """Decorator weapper"""
    @wraps(func)
    def wrapper(url):
        """ Increase the count for the URL """
        cache_redis.incr(f"count:{url}")
        """ Call the original function to fetch the page content """
        return func(url)
    return wrapper


def cache_result(expiration_time):
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            # Check if the result is already cached
            cached_result = cache_redis.get(url)
            if cached_result is not None:
                return cached_result.decode()

            # Call the original function to fetch the page content
            result = func(url)
            # Cache the result with the specified expiration time
            cache_redis.setex(url, expiration_time, result)
            return result
        return wrapper
    return decorator


@cache_result(expiration_time=10)
@track_url_access
def get_page(url: str) -> str:
    """
    uses the requests module to obtain the HTML content of a URL and returns it
    """
    response = requests.get(url)
    return response.text
