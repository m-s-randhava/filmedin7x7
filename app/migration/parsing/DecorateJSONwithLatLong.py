__author__ = 'mohanrandhava'

import csv
import json
import os.path
from pyproj import Proj

"""
DecorateJSONwithLatLong converts the data in 'json_locations_file' and decorates
each record with additional coordinate data for each json record found in
'json_coord_file,' where the key linking the data is 'filmid' which uniquely id's
each film.
"""

class DecorateJSONwithLatLong(object):

    def __init__(self, json_locations_file, json_coord_file):
        self.json_locations_file = json_locations_file
        self.json_coord_file = json_coord_file
        self.json_locations_file_decorated = 'film_locations_in_san_francisco_decorated.json'
        self.mercator_projector = Proj(proj='utm', zone=10, ellps='WGS84')

    def read_data(self):
        basepath = os.path.dirname(__file__)
        locations_coord_filepath = os.path.abspath(os.path.join(basepath, "../..", "data", self.json_coord_file))

        with open(locations_coord_filepath, 'r') as f:
            location_coords = [row for row in f]

        basepath = os.path.dirname(__file__)
        locations_filepath = os.path.abspath(os.path.join(basepath, "../..", "data", self.json_locations_file))

        with open(locations_filepath, 'r') as f:
            locations = [row for row in f]

        basepath = os.path.dirname(__file__)
        locations_decorated_filepath = os.path.abspath(os.path.join(basepath, "../..", "data", self.json_locations_file_decorated))

        print len(location_coords)
        print len(locations)

        locations_hash = dict()
        for l in locations:
            l_json = json.loads(l)
            locations_hash[l_json['filmid']] = l_json

        counter = 0
        with open(locations_decorated_filepath, 'w') as f:
            for lc in location_coords:
                lc_json = json.loads(lc)
                if lc_json['results']:
                    l = locations_hash[lc_json['filmid']]
                    if l:
                        l['location'] = lc_json['results'][0]['geometry']['location']
                        x,y = self.mercator_projector(lc_json['results'][0]['geometry']['location']['lng'],lc_json['results'][0]['geometry']['location']['lat'])
                        l['location_mercator'] = { "x" : x, "y" : y}
                        f.write(json.dumps(l))
                        f.write('\n')
                        counter += 1
                    else:
                        print str(lc_json['filmid']) + " not found\n"
                else:
                    print "No results for " + str(lc_json['filmid']) + "\n"

        print "Decorated " + str(counter) + " lines"

        return

p = DecorateJSONwithLatLong("film_locations_in_san_francisco.json", "film_locations_in_san_francisco_coord.json")
p.read_data()