#!/usr/bin/env python3
""" Redis client
"""
import redis
from uuid import uuid4
from functools import wraps
from typing import Any, Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """ Method that count calls.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **keywords):
        """ Method wrapper.
        """
        self._redis.incr(key)
        return method(self, *args, **keywords)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Method that store the history of inputs and outputs
        for a particular function.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """ Method wrapper.
        """
        self._redis.rpush("{}:inputs".format(key), str(args))
        history = method(self, *args)
        self._redis.rpush("{}:outputs".format(key),
                          str(history))
        return history
    return wrapper



class Cache:
    """ Caching class
    """
    def __init__(self) -> None:
        """ Initialize new cache object
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @count_calls
    @call_history
    def store(self, data: Union[str, bytes,  int,  float]) -> str:
        """ Stores data in redis with randomly generated key
        """
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """ This callable will be used to convert
            the data back to the desired format.
            Args:
                key: string type.
                fn: Optional[Callable].
            Return:
                The convert data.
        """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, data: bytes) -> str:
        """ Method that get a string from bytes.
        """
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """ Method that get a int from bytes.
        """
        return int.from_bytes(data, byteorder)

