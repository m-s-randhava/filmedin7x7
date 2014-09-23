__author__ = 'mohanrandhava'

import sys
from flask.ext.restful import Resource, reqparse
from flask import g
from time import time
from pyproj import Proj

"""
REST API ENDPOINT: FindNearest7FilmsAtLocation

PROVIDES 7 films which are geographically closes to given provided
location.

    ->  Requires latitude/longitude coordinates to service request
"""
class FindNearest7FilmsAtLocation(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(FindNearest7FilmsAtLocation, self).__init__()

    def get(self, lat, lat_sign, lng, lng_sign):
        """
        Because of a quirk in the way that Flask currently route
        matches requests (although you can specify a float type it
        will not accept signed floats) we need to pass lat/lng
        values in absolute value and send their actual signs separately.

        :param - lat
            Latitude coordinate in absolute value
        :param - lat_sign
            Latitude sign (positive or negative)
        :param - lng
            Longitude coordinate in absolute value
        :param - lng_sign
            Longitude sign (positive or negative)

        RETURNS list of 7 json results with each entry comprising full film
        metadata for the films which were located closest to provided data.
        """
        time1 = time()
        print "INSIDE"
        #   Converting Lat/Lng back to original signs
        lat = lat if lat_sign == "p" else (-1 * lat)
        lng = lng if lng_sign == "p" else (-1 * lng)

        #   Converting provided Lat/Lng into UTM (Universal Transverse Mercator)
        #   encoding to place the points in a 2D grid, since this service will
        #   leverage a KD tree which will expect the data to be points in 2D
        p = Proj(proj='utm', zone=10, ellps='WGS84')
        lat_mercator,lng_mercator = p(lng, lat)

        points_locations = []
        #   Wrap the access to the in-memory KD tree in try/catch if for any reason
        #   the KD tree throws some error or exception
        try:
            #   Query the KD Tree for nearest 7 points
            points_locations =  g.filmlocationsKDTree.find_nn((lat_mercator, lng_mercator),7)
        except:
            e = sys.exc_info()[0]

        #   Once the KD Tree has found the closest 2D points associated
        #   with films, we need to lookup which films are associated with
        #   those points by querying an inverted hash table of points
        #   to films
        _7films_nearest_me = []
        location_to_film_mapping = {}
        for pLocation in points_locations:
            films_at_location = g.invertedPointLocationIndex.lookup_locations(pLocation)

            #   There may be many films that were shot at the same location.
            #   If so, the KD tree will store those same points separately, so
            #   that if 3 films were shot at a particular location, 3 of the same
            #   points will be returned.  In which case, we will need to retrieve
            #   all 3 films.  The inverted hash table maps points in 2D to an array
            #   of possible films filmed at that location.  As such, then, we need
            #   to iterate over all films at that location.
            if pLocation in location_to_film_mapping:
                location_to_film_mapping[pLocation]['index'] += 1
                index = location_to_film_mapping[pLocation]['index']
            else:
                location_to_film_mapping[pLocation] = {}
                location_to_film_mapping[pLocation]['films'] = films_at_location
                location_to_film_mapping[pLocation]['index'] = 0
                index = 0
            _7films_nearest_me.append(location_to_film_mapping[pLocation]['films'][index])

        time2 = time()

        print '%s function took %0.3f ms' % ("FindNearestAPI.FindNearest7", (time2-time1)*1000.0)
        print _7films_nearest_me

        return _7films_nearest_me