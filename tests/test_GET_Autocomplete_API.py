import unittest
import os
import json
from flask import url_for
from app import create_app

class test_GET_Film_Locations_API(unittest.TestCase):
    def setUp(self):
        self.mysql_results_file_for_Mar = 'found_locations_mysql_prefix_Mar.txt'
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_request_multiple_matching_locations(self):
        """ TESTING IF Autocomplete API will return all 'Locations' which have
            words within starting with 'mar' (case-insensitive)

            COMPARING WITH data retrieved from data loaded into MySQL from
            raw file 'film_locations_in_san_francisco.csv' which was
            downloaded from site @ https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am?

            The comparison data was retrieved from MySQL using the following
            query:

            SELECT Locations FROM Locations WHERE Locations REGEXP '[[:<:]]Mar.*'
        """
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../app", "data", self.mysql_results_file_for_Mar))
        f = open(filepath, 'r')

        mysql_locations_results = f.readlines()

        expected_response_as_json = [mysql_locations_result.strip(' \t\n\r') for mysql_locations_result in mysql_locations_results]
        response = self.client.get(url_for('filmlocations_auto_complete') + '?term=mar')
        received_response_as_json = json.loads(response.get_data())
        received_response_as_json = [ r_r_as_json.encode('ascii').strip(' \t\n\r') for r_r_as_json in received_response_as_json]
        self.assertEquals(set(expected_response_as_json), set(received_response_as_json))

    def test_request_multiple_locations(self):
        """ TESTING IF Autocomplete API will return all 'Locations' which have
            words within starting with 'zzzz' (case-insensitive)

            COMPARING WITH an empty array
        """
        expected_response_as_json = []
        response = self.client.get(url_for('filmlocations_auto_complete') + '?term=zzzz')
        received_response_as_json = json.loads(response.get_data())
        received_response_as_json = [ r_r_as_json.encode('ascii').strip(' \t\n\r') for r_r_as_json in received_response_as_json]
        self.assertEquals(set(expected_response_as_json), set(received_response_as_json))


