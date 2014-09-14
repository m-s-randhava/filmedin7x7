__author__ = 'mohanrandhava'

from unittest import TestCase

import os.path
from app.storage.redis import RedisStore
from app.migration.loadRedis import LoadRedis
from app import create_app
from flask import current_app

class TestSearchRedis(TestCase):

    def setUp(self):
        self.mysql_results_file = 'found_locations_mysql_prefix_Mar.txt'
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_search(self):
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../app", "data", self.mysql_results_file))
        f = open(filepath, 'r')

        print 'Loading data (may take a few seconds...)'
        l = LoadRedis(os.getenv('FLASK_CONFIG') or 'default','film_locations_in_san_francisco_decorated.json','film_locations_in_san_francisco_coord.json')
        l.load_locations_prefixes_into_redis()

        rStore = RedisStore(current_app.config['REDIS_AUTOCOMPLETE_SORTED_SET'])

        mysql_locations_results = f.readlines()
        mysql_locations_results = [mysql_locations_result.strip(' \t\n\r') for mysql_locations_result in mysql_locations_results]
        redis_results = rStore.search('Mar')
        redis_locations_results = [redis_result['Locations'] for redis_result in redis_results]
        redis_locations_results = [redis_locations_result.encode('ascii').strip(' \t\n\r') for redis_locations_result in redis_locations_results]
        redis_locations_results = sorted(redis_locations_results)

        for index in range(len(redis_locations_results)):
            if mysql_locations_results[index] != redis_locations_results[index]:
                print "alert:   " + mysql_locations_results[index] + "!=" + redis_locations_results[index] + "x"

        self.assertTrue(set(mysql_locations_results) == set(redis_locations_results))

    def tearDown(self):
        self.app_context.pop()