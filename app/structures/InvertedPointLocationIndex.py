__author__ = 'mohanrandhava'

import json
import os.path

class InvertedPointLocationIndex(object):

    def __init__(self):
        self.json_locations_file_decorated = 'film_locations_in_san_francisco_decorated.json'

    def build_inverted_location_index(self):
        basepath = os.path.dirname(__file__)
        locations_decorated_filepath = os.path.abspath(os.path.join(basepath, "..", "data", self.json_locations_file_decorated))

        with open(locations_decorated_filepath, 'r') as f:
            locations = [row for row in f]

        counter = 0
        self.invertedPointLocationIndex = {}
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

    def lookup_location(self,point):
        return self.invertedPointLocationIndex[point]
