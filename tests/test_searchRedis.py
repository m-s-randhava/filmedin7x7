__author__ = 'mohanrandhava'

from unittest import TestCase

import os.path
from app.storage.redis import RedisStore
from app.migration.loadRedis import LoadRedis
from app import create_app
from flask import current_app

class TestSearchRedis(TestCase):

    def setUp(self):
        self.mysql_results_file_for_Mar = 'found_locations_mysql_prefix_Mar.txt'
        self.mysql_results_file_for_A = 'found_locations_mysql_prefix_a.txt'
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        l = LoadRedis(os.getenv('FLASK_CONFIG') or 'default','film_locations_in_san_francisco_decorated.json','film_locations_in_san_francisco_coord.json')
        l.load_locations_prefixes_into_redis()

    def test_basic_search(self):
        """ TESTING IF redis will return all 'Locations' which have words
            within starting with 'a'

            COMPARING WITH data retrieved from data loaded into MySQL from
            raw file 'film_locations_in_san_francisco.csv' which was
            downloaded from site @ https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am?

            The comparison data was retrieved from MySQL using the following
            query:

            SELECT Locations FROM Locations WHERE Locations REGEXP '[[:<:]]a' ORDER BY Locations ASC
        """
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../app", "data", self.mysql_results_file_for_A))
        f = open(filepath, 'r')

        rStore = RedisStore(current_app.config['REDIS_AUTOCOMPLETE_SORTED_SET'], current_app.config['REDIS_HOSTNAME'], current_app.config['REDIS_PORT'], current_app.config['REDIS_DB'], current_app.config['REDIS_PASSWORD'])

        mysql_locations_results = f.readlines()
        mysql_locations_results = [mysql_locations_result.strip(' \t\n\r') for mysql_locations_result in mysql_locations_results]
        redis_results = rStore.search('a')
        redis_locations_results = [redis_result['Locations'] for redis_result in redis_results]
        redis_locations_results = [redis_locations_result.encode('ascii').strip(' \t\n\r') for redis_locations_result in redis_locations_results]
        redis_locations_results = sorted(redis_locations_results)

        self.assertEquals(set(mysql_locations_results),set(redis_locations_results))

    def test_search(self):
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../app", "data", self.mysql_results_file_for_Mar))
        f = open(filepath, 'r')

        rStore = RedisStore(current_app.config['REDIS_AUTOCOMPLETE_SORTED_SET'], current_app.config['REDIS_HOSTNAME'], current_app.config['REDIS_PORT'], current_app.config['REDIS_DB'], current_app.config['REDIS_PASSWORD'])

        mysql_locations_results = f.readlines()
        mysql_locations_results = [mysql_locations_result.strip(' \t\n\r') for mysql_locations_result in mysql_locations_results]
        redis_results = rStore.search('Mar')
        redis_locations_results = [redis_result['Locations'] for redis_result in redis_results]
        redis_locations_results = [redis_locations_result.encode('ascii').strip(' \t\n\r') for redis_locations_result in redis_locations_results]
        redis_locations_results = sorted(redis_locations_results)

        self.assertEquals(set(mysql_locations_results),set(redis_locations_results))

    def tearDown(self):
        self.app_context.pop()