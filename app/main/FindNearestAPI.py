__author__ = 'mohanrandhava'

import sys
from flask.ext.restful import Resource, reqparse
from flask import g
from time import time
from pyproj import Proj

class FindNearest7(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(FindNearest7, self).__init__()

    def get(self, lat, lat_sign, lng, lng_sign):
        time1 = time()

        lat = lat if lat_sign == "p" else (-1 * lat)
        lng = lng if lng_sign == "p" else (-1 * lng)

        print ">>>   Lat:   " + str(lat) + ", Lng:   " + str(lng)

        p = Proj(proj='utm', zone=10, ellps='WGS84')
        lat_mercator,lng_mercator = p(lng, lat)

        points_locations = []
        try:
            points_locations =  g.filmlocationsKDTree.find_nn((lat_mercator, lng_mercator),7)
            print points_locations
        except:
            e = sys.exc_info()[0]

        _7films_nearest_me = []
        location_to_film_mapping = {}
        for pLocation in points_locations:
            films_at_location = g.invertedPointLocationIndex.lookup_location(pLocation)
            # print films_at_location
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