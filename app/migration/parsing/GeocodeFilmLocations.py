__author__ = 'mohanrandhava'

import urllib
import urllib2
import json
import time
import sys
import os.path

"""
GeoCodeFilmLocations queries google for the coordinates of each film location
found in each json record at location['Locations'] in 'locations_json_file' and stores
the retrieved geocoded data for each record in the fil locations_geocoded_json_file,'
where the key linking the data is 'filmid' which uniquely id's each film.
"""
class GeoCodeFilmLocations(object):

    def __init__(self, locations_json_file, locations_geocoded_json_file):
        self.locations_json_file = locations_json_file
        self.locations_geocoded_json_file = locations_geocoded_json_file

    def get_geocode_data_for_locations(self):
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../..", "data", self.locations_json_file))
        json_file = open(filepath, 'r')

        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../..", "data", self.locations_geocoded_json_file))
        geocoded_json_file = open(filepath, 'w')

        counter = 0
        for json_string in json_file:
            json_object = json.loads(json_string)
            location = json_object['Locations']
            counter += 1
            if not location:
                print json.dumps({'filmid':json_object['filmid']})
            else:
                print "...geocoding location:   " + location
                query_args = { 'address': location, 'components' : 'locality:San Francisco', 'key' : 'AIzaSyDRbW9fMk41wOIJ0xY5EOsofKpFQ5yK3Ns' }
                query_args_enc = urllib.urlencode(query_args)
                url = 'https://maps.googleapis.com/maps/api/geocode/json?%s' % query_args_enc
                print url

                print "...starting geocoding"
                try:
                    response = urllib2.urlopen(url)
                except urllib2.HTTPError, e:
                    print e.code
                except urllib2.URLError, e:
                    print e.args
                print "...ended geocoding"

                json_geocode = response.read()
                json_geocode_object = json.loads(json_geocode)
                json_geocode_object['filmid'] = json_object['filmid']
                json_geocode_line = json.dumps(json_geocode_object)

                print "...writing result to file..."
                geocoded_json_file.write(json_geocode_line)
                geocoded_json_file.write("\n")
                print "...waiting 1 second..."
                time.sleep(1)

g = GeoCodeFilmLocations('film_locations_in_san_francisco.json','film_locations_in_san_francisco_coord.json')
print g.get_geocode_data_for_locations()