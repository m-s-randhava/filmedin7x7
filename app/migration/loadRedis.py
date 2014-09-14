__author__ = 'mohanrandhava'

import re
import json
import os.path
from redis_completion import RedisEngine
from config import config

class LoadRedis(object):

    def __init__(self, config_name, locations_json_file, locations_geocoded_json_file):
        self.locations_json_file = locations_json_file
        self.locations_geocoded_json_file = locations_geocoded_json_file
        self.engine = RedisEngine(prefix=config[config_name].REDIS_AUTOCOMPLETE_SORTED_SET,stop_words=None,cache_timeout=300,port=11827)
        self.engine.flush()

    def load_locations_prefixes_into_redis(self):
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "..", "data", self.locations_json_file))
        json_file = open(filepath, 'r')

        for json_string in json_file:
            json_object = json.loads(json_string)
            location = json_object['Locations']
            if location and location.strip() != 'None':
                location = re.sub(r'([^\s\w]|_|-)+', ' ', location)
                self.engine.store_json(json_object['filmid'], location, json_object) # id, search phrase, data


