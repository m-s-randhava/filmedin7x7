import unittest
import json
import urllib
from flask import current_app, url_for
from app import create_app

class test_GET_Film_Locations_API_Redis_UA(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing_redis_ua')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_request_redis_unavailable(self):
        response = self.client.get(url_for('film_locations',location='mar') + '?page=1')
        expected_response = []
        self.assertEquals(expected_response, json.loads(response.get_data()))
        self.assertEquals(0, int(response.headers.get('prev')))
        self.assertEquals(0, int(response.headers.get('next')))
        self.assertEquals(1, int(response.headers.get('page')))
        self.assertEquals(0, int(response.headers.get('pages')))
        self.assertEquals(0, int(response.headers.get('num_films_at_locations')))