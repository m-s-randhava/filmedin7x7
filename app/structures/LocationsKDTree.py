__author__ = 'mohanrandhava'

import json
import os.path
import scipy.spatial as ss

class LocationsKDTree(object):

    def __init__(self):
        self.json_locations_file_decorated = 'film_locations_in_san_francisco_decorated.json'

    def load_point_data(self):
        basepath = os.path.dirname(__file__)
        locations_decorated_filepath = os.path.abspath(os.path.join(basepath, "..", "data", self.json_locations_file_decorated))

        with open(locations_decorated_filepath, 'r') as f:
            locations = [row for row in f]

        counter = 0
        self.mercatorPointsArray = []
        for l in locations:
            l_json = json.loads(l)
            if l_json:
                self.mercatorPointsArray.append((l_json['location_mercator']['x'],l_json['location_mercator']['y']))
                counter += 1
            else:
                print str(l_json) + " mal-formed\n"

        return

    def build_kd_tree(self):
        self.kdtree = ss.KDTree(self.mercatorPointsArray)
        return

    def find_nn(self,point, nearest):
        nearest_nn_indices = self.kdtree.query([point], nearest)
        points = [self.mercatorPointsArray[nn] for nn in nearest_nn_indices[1][0]]
        return points
