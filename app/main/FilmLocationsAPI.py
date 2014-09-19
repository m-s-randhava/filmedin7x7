__author__ = 'mohanrandhava'

from flask.ext.restful import Resource, reqparse
from app.storage.redis import RedisStore
from flask import current_app, request, g
import urllib

class FilmLocations(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(FilmLocations, self).__init__()

    def get(self, location):
        page = int(request.args.get('page'))
        location = urllib.unquote(location).decode('utf8')

        points_locations =  g.filmlocationsKDTree.find_nn((552048.7215749588, 4182698.120068086),7)
        print g.invertedPointLocationIndex.lookup_location(points_locations[0])
        print g.invertedPointLocationIndex.lookup_location(points_locations[1])
        print g.invertedPointLocationIndex.lookup_location(points_locations[2])
        print g.invertedPointLocationIndex.lookup_location(points_locations[3])
        print g.invertedPointLocationIndex.lookup_location(points_locations[4])
        print g.invertedPointLocationIndex.lookup_location(points_locations[5])
        print g.invertedPointLocationIndex.lookup_location(points_locations[6])

        r_store = RedisStore(current_app.config['REDIS_AUTOCOMPLETE_SORTED_SET'], current_app.config['REDIS_HOSTNAME'], current_app.config['REDIS_PORT'], current_app.config['REDIS_DB'], current_app.config['REDIS_PASSWORD'])
        film_locations = r_store.search(location)
        num_film_locations = len(film_locations)

        start = 10 * (page - 1)
        end = (start + 10) if (start + 10) < num_film_locations else num_film_locations

        return film_locations[start:end]