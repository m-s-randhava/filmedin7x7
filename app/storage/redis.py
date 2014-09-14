__author__ = 'mohanrandhava'

from redis_completion import RedisEngine

class RedisStore(object):

    def __init__(self, prefix):
        self.engine = RedisEngine(prefix)


    def search(self, p, **kwargs):
        return self.engine.search_json(p, **kwargs)
