__author__ = 'mohanrandhava'

import sys
from redis_completion import RedisEngine

"""
Redis Exception: for RedisEngine

EXCEPTION to be rethrown if an error or exception
is caught while querying underlying RedisEngine.

Purposefully as generic as possible.
"""
class RedisException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


"""
Redis Autocompletion Storage DAO: RedisStore

ABSTRACTS search access to a Redis instance by wrapping a
redis-completion RedisEngine that has been instantiated to
point to a structured erected upon a particular field of
information, e.g. 'Locations'

"""
class RedisStore(object):

    def __init__(self, prefix, host, port, db, password):
        """
        :param - prefix
            Field/Column of data for which autocompletion search results are to
            be queried
        :param - host
            Redis hostname
        :param - port
            Redis port
        :param - db
            Redis db
        :param - password
            Redis password
        """
        self.engine = RedisEngine(prefix, stop_words=set(), cache_timeout=300, host=host, port=port, db=db, password=password)
        # self.engine = RedisEngine(prefix, stop_words=None, cache_timeout=300, host=host, port=port, db=db, password=password)


    def search(self, p, **kwargs):
        results = []

        #   Perform query, wrap in try/catch in case there is an error accessing.
        try:
            results = self.engine.search_json(p, **kwargs)
        except:
            e = sys.exc_info()[0]
            raise RedisException('Problem reaching redis')

        return results
