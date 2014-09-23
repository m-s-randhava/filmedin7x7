__author__ = 'mohanrandhava'

import unittest
from app.structures.InvertedPointLocationIndex import InvertedPointLocationIndex, LookupException

class testLocationsKDTree(unittest.TestCase):

    def setUp(self):
        self.test = InvertedPointLocationIndex()
        self.point_data = self.test.build_inverted_location_index()

    def test_lookup_location_single_entry(self):
        found_location = self.test.lookup_locations((547809.3901228452, 4180255.2775678867))
        self.assertEqual(found_location, [{u'Fun Facts': u"Golden Gate Park is similar in shape but 20% larger than New York's Central Park.", u'Actor 2': u'Jayden C. Smith', u'Title': u'The Pursuit of Happyness', u'Production Company': u'Columbia Pictures Corporation', u'Writer': u'Gabriele Muccino', u'Locations': u"Golden Gate Park Children's Playground ", u'Director': u'Steven Conrad', u'filmid': 941, u'Actor 1': u'Will Smith', u'location_mercator': {u'y': 4180255.2775678867, u'x': 547809.3901228452}, u'Actor 3': u'', u'Distributor': u'Columbia Pictures', u'Release Year': u'2006', u'location': {u'lat': 37.7683778, u'lng': -122.4571623}}])

        found_location = self.test.lookup_locations((548452.309670817, 4184076.543236543))
        self.assertEqual(found_location, [{u'Fun Facts': u'Suppsedly, the Cow Palace\'s name derives from a newspaper editorial in which the writer wonders whether the soon-to-be-built structure for livestock was a "palace for cows". ', u'Actor 2': u'Ed Harris', u'Title': u'The Right Stuff', u'Production Company': u'The Ladd Company', u'Writer': u'Philip Kaufman', u'Locations': u'Cow Palace', u'Director': u'Philip Kaufman', u'filmid': 943, u'Actor 1': u'Sam Shepard', u'location_mercator': {u'y': 4184076.543236543, u'x': 548452.309670817}, u'Actor 3': u'', u'Distributor': u'The Ladd Company', u'Release Year': u'1983', u'location': {u'lat': 37.8027843, u'lng': -122.4496074}}])

    def test_lookup_location_multiple_entry(self):
        found_location = self.test.lookup_locations((551392.6450425778, 4181595.6111473767))
        self.assertEqual(found_location, [{u'Fun Facts': u'The Dalai Lama opened an exhibition on Wisdom and Compassion at the museum in 1991.', u'Actor 2': u'Chevy Chase', u'Title': u'Foul Play', u'Production Company': u'Paramount Pictures', u'Writer': u'Colin Higgins', u'Locations': u'Asian Art Museum (200 Larkin Street, Civic Center)', u'Director': u'Colin Higgins', u'filmid': 313, u'Actor 1': u'Goldie Hawn', u'location_mercator': {u'y': 4181595.6111473767, u'x': 551392.6450425778}, u'Actor 3': u'', u'Distributor': u'Paramount Pictures', u'Release Year': u'1978', u'location': {u'lat': 37.7802635, u'lng': -122.4163842}}, {u'Fun Facts': u'The Dalai Lama opened an exhibition on Wisdom and Compassion at the museum in 1991.', u'Actor 2': u'Mandy Patinkin', u'Title': u'Maxie', u'Production Company': u'Elsboy Entertainment', u'Writer': u'Patricia Resnick', u'Locations': u'Asian Art Museum (200 Larkin Street, Civic Center)', u'Director': u'Paul Aaron', u'filmid': 541, u'Actor 1': u'Glenn Close', u'location_mercator': {u'y': 4181595.6111473767, u'x': 551392.6450425778}, u'Actor 3': u'Gary Oldman', u'Distributor': u'Orion Pictures Corporation', u'Release Year': u'1985', u'location': {u'lat': 37.7802635, u'lng': -122.4163842}}])

    def test_lookup_location_errors(self):
        self.assertRaises(LookupException, self.test.lookup_locations, (1,2))

if __name__ == '__main__':
    unittest.main()