__author__ = 'mohanrandhava'

from redis_completion import RedisEngine

class RedisStore(object):

    def __init__(self, prefix, host, port, db, password):
        self.engine = RedisEngine(prefix, stop_words=None, cache_timeout=300, host=host, port=port, db=db, password=password)


    def search(self, p, **kwargs):
        return self.engine.search_json(p, **kwargs)
