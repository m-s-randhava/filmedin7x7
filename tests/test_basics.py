import unittest
from flask import current_app, url_for
from app import create_app

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_home_page(self):
        response = self.client.get(url_for('main.index'))
        self.assertTrue('Find Nearest 7 Movie Locations' in response.get_data(as_text=True))