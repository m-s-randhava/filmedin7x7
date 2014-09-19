__author__ = 'mohanrandhava'

import unittest
from app.structures.LocationsKDTree import LocationsKDTree

class testLocationsKDTree(unittest.TestCase):

    def setUp(self):
        self.test = LocationsKDTree()
        self.test.mercatorPointsArray = [(552084.9682165304, 4182494.1939107366), (551922.8858612546, 4182574.0555520994), (551687.9949461814, 4182217.968801949),
                                         (552775.8082342255, 4183336.7417580322), (553222.9632670761, 4183422.393102693), (552198.7222675259, 4184064.8048690264),
                                         (549362.9961397024, 4181902.574203599), (548023.1142878283, 4180961.314933798), (551183.5342344284, 4184494.9211385823),
                                         (548547.6683833781, 4179180.1576283425), (549558.9617763544, 4184499.9538624967), (553803.7182814779, 4180131.3817638056),
                                         (552354.47799122, 4184532.357535243), (550631.7088304324, 4182068.2753886213), (550951.7531905753, 4181648.8476454713)]
        self.test.build_kd_tree()

    def test_lookup_location(self):
        nearest_nn_points = self.test.find_nn((552048.7215749588, 4182698.120068086),5)
        self.assertEqual(nearest_nn_points[0],(551922.8858612546, 4182574.0555520994))
        self.assertEqual(nearest_nn_points[1],(552084.9682165304, 4182494.1939107366))
        self.assertEqual(nearest_nn_points[2],(551687.9949461814, 4182217.968801949))
        self.assertEqual(nearest_nn_points[3],(552775.8082342255, 4183336.7417580322))
        self.assertEqual(nearest_nn_points[4],(552198.7222675259, 4184064.8048690264))

if __name__ == '__main__':
    unittest.main()