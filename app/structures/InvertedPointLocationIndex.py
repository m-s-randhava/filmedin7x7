__author__ = 'mohanrandhava'

import json
import os.path
import sys

"""
Lookup Exception: for InvertedPointLocationIndex

EXCEPTION to be rethrown if an error or exception
is caught while querying underlying InvertedPointLocationIndex.

Purposefully as generic as possible.
"""
class LookupException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


"""
Inverted Index: InvertedPointLocationIndex

MAPS film location UTM lat/lng points to filmlocations.

"""
class InvertedPointLocationIndex(object):

    def __init__(self):
        #   File which contains filmlocations decorated with calculated UTM coordinates
        self.json_locations_file_decorated = 'film_locations_in_san_francisco_decorated.json'

    def build_inverted_location_index(self):
        basepath = os.path.dirname(__file__)
        locations_decorated_filepath = os.path.abspath(os.path.join(basepath, "..", "data", self.json_locations_file_decorated))

        with open(locations_decorated_filepath, 'r') as f:
            locations = [row for row in f]

        counter = 0
        self.invertedPointLocationIndex = {}

        #   There may be many films that were filmed at a particular locations.
        #   As such, we need to have a hash table mapping that maps points
        #   to an array of possible locations.
        #   For each location we see if that location has already been added,
        #   in which case we simply append to the existing array at that location,
        #   else we create a new array inserted at that position with the new
        #   location entry.
        for l in locations:
            l_json = json.loads(l)
            if l_json:
                key = (l_json['location_mercator']['x'],l_json['location_mercator']['y'])
                if key in self.invertedPointLocationIndex:
                    self.invertedPointLocationIndex[key].append(l_json)
                else:
                    self.invertedPointLocationIndex[key] = []
                    self.invertedPointLocationIndex[key].append(l_json)
                counter += 1
            else:
                print str(l_json) + " mal-formed\n"

        return

    def lookup_locations(self,point):
        locations = []

        #   Lookup location by point
        #   Wrap in try/catch to trap any errors that may arise while accessing
        #   the hash table.
        try:
            locations = self.invertedPointLocationIndex[point]
        except:
            e = sys.exc_info()[0]
            raise LookupException('this is the error message')

        return locations
