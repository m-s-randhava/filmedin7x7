__author__ = 'mohanrandhava'

import re
import json
import os.path
from redis_completion import RedisEngine
from config import config

"""
Migration File: LoadRedisWithLocationPrefixes

LOADS Redis instance with location prefixes via the
redis-completion RedisEngine that will provide
autocompletion based upon those prefixes.

    ->  Requires a file of json records, where each record
        has a 'Locations' entry
    ->  Breaks word or words into their respective prefixes
        and loads Redis with those prefixes
"""

class LoadRedisWithLocationPrefixes(object):

    def __init__(self, config_name, locations_json_file, locations_geocoded_json_file):
        self.locations_json_file = locations_json_file
        self.locations_geocoded_json_file = locations_geocoded_json_file

        #   The RedisEngine is instantiated that will perform 'autocompletion'
        #   critical: No stop words are specified, as it was discovered via
        #   testing that running with the default 'stop_words=None' still
        #   associates a default set of stopwords to be utilized, one entry
        #   of which is 'a' which precludes autocompletion when a simple 'a'
        #   is provided.
        self.engine = RedisEngine(prefix=config[config_name].REDIS_AUTOCOMPLETE_SORTED_SET, stop_words=set(), cache_timeout=300, host=config[config_name].REDIS_HOSTNAME, port=config[config_name].REDIS_PORT, db=config[config_name].REDIS_DB, password=config[config_name].REDIS_PASSWORD)
        # self.engine = RedisEngine(prefix=config[config_name].REDIS_AUTOCOMPLETE_SORTED_SET, stop_words=None, cache_timeout=300, host=config[config_name].REDIS_HOSTNAME, port=config[config_name].REDIS_PORT, db=config[config_name].REDIS_DB, password=config[config_name].REDIS_PASSWORD)
        self.engine.flush()

    def load_locations_prefixes_into_redis(self):
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "..", "data", self.locations_json_file))
        json_file = open(filepath, 'r')

        #   Iterate over all filmlocation json entries and extract the 'Locations' entry from the
        #   json object, strip the phrase of all non-alphanumeric characters before inserting into
        #   Redis.
        for json_string in json_file:
            json_object = json.loads(json_string)
            location = json_object['Locations']
            if location and location.strip() != 'None':
                location = re.sub(r'([^\s\w]|_|-)+', ' ', location)
                # Store the filmid (unique), search phrase, full metadata for filmlocation
                self.engine.store_json(json_object['filmid'], location, json_object)


