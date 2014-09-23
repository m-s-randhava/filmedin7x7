import unittest
import os
import json
from flask import url_for
from app import create_app

class test_GET_Film_Locations_API_Redis_UA(unittest.TestCase):
    def setUp(self):
        self.mysql_results_file_for_Mar = 'found_locations_mysql_prefix_Mar.txt'

        #   The configuration where Redis is improperly configured
        self.app = create_app('testing_redis_ua')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_request_redis_unavailable(self):
        """ TESTING IF the application gracefully handles an 'unavailable' redis instance
            by throwing an exception

            VERIFIED by detecting that the expected response is an empty array
        """
        expected_response_as_json = []
        response = self.client.get(url_for('filmlocations_auto_complete') + '?term=mar')
        received_response_as_json = json.loads(response.get_data())
        received_response_as_json = [ r_r_as_json.encode('ascii').strip(' \t\n\r') for r_r_as_json in received_response_as_json]
        self.assertEquals(set(expected_response_as_json), set(received_response_as_json))


