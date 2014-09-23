import unittest
import os
import json
from flask import url_for
from app import create_app

class test_GET_Film_Locations_API_Redis_UA(unittest.TestCase):
    def setUp(self):
        self.mysql_results_file_for_Mar = 'found_locations_mysql_prefix_Mar.txt'
        self.app = create_app('testing_redis_ua')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_request_redis_unavailable(self):
        """ TESTING IF Autocomplete API will return all 'Locations' which have
            words within starting with 'mar' (case-insensitive)

            COMPARING WITH data retrieved from data loaded into MySQL from
            raw file 'film_locations_in_san_francisco.csv' which was
            downloaded from site @ https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am?

            The comparison data was retrieved from MySQL using the following
            query:

            SELECT Locations FROM Locations WHERE Locations REGEXP '[[:<:]]Mar.*'
        """
        expected_response_as_json = []
        response = self.client.get(url_for('filmlocations_auto_complete') + '?term=mar')
        received_response_as_json = json.loads(response.get_data())
        received_response_as_json = [ r_r_as_json.encode('ascii').strip(' \t\n\r') for r_r_as_json in received_response_as_json]
        self.assertEquals(set(expected_response_as_json), set(received_response_as_json))


