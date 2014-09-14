__author__ = 'mohanrandhava'

from flask.ext.restful import Resource, reqparse
from app.storage.redis import RedisStore
from flask import current_app, request, jsonify

class FilmLocations(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(FilmLocations, self).__init__()

    def get(self, location):
        page = int(request.args.get('page'))
        results_per_page = current_app.config['RESULTS_PER_PAGE']
        r_store = RedisStore(current_app.config['REDIS_AUTOCOMPLETE_SORTED_SET'])
        film_locations = r_store.search(location)
        num_film_locations = len(film_locations)

        pages = num_film_locations/results_per_page
        pages = (pages + 1) if num_film_locations % results_per_page > 0 else pages

        if (page - 1) >= 1:
            prev = page - 1
        else:
            prev = 0
        if (page + 1) <= pages:
            next = page + 1
        else:
            next = 0

        start = 10 * (page - 1)
        end = start + 9

        return jsonify({
            'filmlocations' : film_locations[start:end],
            'prev' : prev,
            'next' : next,
            'count' : num_film_locations
        })