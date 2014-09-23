import unittest
import json
import os
from flask import current_app, url_for
from app import create_app
from app.structures.LocationsKDTree import LocationsKDTree
from app.structures.InvertedPointLocationIndex import InvertedPointLocationIndex

class test_GET_Film_Locations_Near_Me_API(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        #   An inverted index, mapping UTM (Universal Transverse Mercator) lat/lng
        #   values geolocating each film, to a LIST of films that were filmed
        #   at that location.
        #
        #   IMPORTANT!:  This is a shared data-structure, built only at startup,
        #   that is READ-ONLY by all, and so can be safely shared.
        invertedPointLocationIndex = InvertedPointLocationIndex()
        invertedPointLocationIndex.build_inverted_location_index()

        #   A KD tree, implemented using the scipy package's kdtree implementation
        #   under the hood, to allow for fast O(ln) queries of 2D point data.  The
        #   points that it stores are geocoded locations coded in UTM to allow them
        #   to be treated as 2D points to an approximation.
        #
        #   IMPORTANT!:  This is a shared data-structure, built only at startup,
        #   that is READ-ONLY by all, and so can be safely shared.
        filmLocationsKDTree = LocationsKDTree()
        filmLocationsKDTree.load_point_data()
        filmLocationsKDTree.build_kd_tree()

        self.app_context.g.filmlocationsKDTree = filmLocationsKDTree
        self.app_context.g.invertedPointLocationIndex = invertedPointLocationIndex

    def tearDown(self):
        self.app_context.pop()

    def test_request_7_locations_near_me(self):


        """ TESTING IF redis will return all 'Locations' which are closest
            to the steps of San Francisco City Hall

            COMPARING WITH the 7 locations manually calculated using
            the 'haversine' formulay on the original lat/lng coordinates
            provided by Google Maps API

            The comparison data was retrieved by calling '__get_expected_7_locations_near_me':
        """
        response = self.client.get(url_for('films_near_me',lat=37.779390,lat_sign='p',lng=122.418432,lng_sign='n'))
        expected_response = self.__get_expected_7_locations_near_me()
        self.assertEquals(expected_response,json.loads(response.get_data()))

    def __get_expected_7_locations_near_me(self):
        """
        The known 7 locations are included in this file: '_7film_locations_near_me_test.txt'
        This file is read and the contents converted to json array.
        """
        basepath = os.path.dirname(__file__)
        locations_coord_filepath = os.path.abspath(os.path.join(basepath, "../app", "data", "_7film_locations_near_me_test.txt"))

        expected_response = ""
        with open(locations_coord_filepath, 'r') as f:
            for row in f:
                expected_response = expected_response + row

        return json.loads(expected_response)