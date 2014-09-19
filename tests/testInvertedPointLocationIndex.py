__author__ = 'mohanrandhava'

import unittest
from app.structures.LocationsKDTree import LocationsKDTree

class testLocationsKDTree(unittest.TestCase):

    def setUp(self):
        self.test = LocationsKDTree()
        self.point_data = self.test.load_point_data()

    def test_lookup_location(self):
        self.test.build_inverted_location_index()
        found_location = self.test.lookup_location((547809.3901228452, 4180255.2775678867))
        self.assertEqual(found_location, {u'Fun Facts': u"Golden Gate Park is similar in shape but 20% larger than New York's Central Park.", u'Actor 2': u'Jayden C. Smith', u'Title': u'The Pursuit of Happyness', u'Production Company': u'Columbia Pictures Corporation', u'Writer': u'Gabriele Muccino', u'Locations': u"Golden Gate Park Children's Playground ", u'Director': u'Steven Conrad', u'filmid': 941, u'Actor 1': u'Will Smith', u'location_mercator': {u'y': 4180255.2775678867, u'x': 547809.3901228452}, u'Actor 3': u'', u'Distributor': u'Columbia Pictures', u'Release Year': u'2006', u'location': {u'lat': 37.7683778, u'lng': -122.4571623}})

        found_location = self.test.lookup_location((548452.309670817, 4184076.543236543))
        self.assertEqual(found_location, {u'Fun Facts': u'Suppsedly, the Cow Palace\'s name derives from a newspaper editorial in which the writer wonders whether the soon-to-be-built structure for livestock was a "palace for cows". ', u'Actor 2': u'Ed Harris', u'Title': u'The Right Stuff', u'Production Company': u'The Ladd Company', u'Writer': u'Philip Kaufman', u'Locations': u'Cow Palace', u'Director': u'Philip Kaufman', u'filmid': 943, u'Actor 1': u'Sam Shepard', u'location_mercator': {u'y': 4184076.543236543, u'x': 548452.309670817}, u'Actor 3': u'', u'Distributor': u'The Ladd Company', u'Release Year': u'1983', u'location': {u'lat': 37.8027843, u'lng': -122.4496074}})

if __name__ == '__main__':
    unittest.main()