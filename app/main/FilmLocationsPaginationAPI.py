__author__ = 'mohanrandhava'

from flask.ext.restful import Resource, reqparse
from app.storage.redis import RedisStore
from flask import current_app, request, jsonify

class FilmLocationsPagination(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(FilmLocationsPagination, self).__init__()

    def get(self, location):
        page = int(request.args.get('page'))
        results_per_page = current_app.config['RESULTS_PER_PAGE']
        r_store = RedisStore(current_app.config['REDIS_AUTOCOMPLETE_SORTED_SET'], current_app.config['REDIS_HOSTNAME'], current_app.config['REDIS_PORT'], current_app.config['REDIS_DB'], current_app.config['REDIS_PASSWORD'])
        film_locations = r_store.search(location)
        num_film_locations = len(film_locations)

        pages = num_film_locations/results_per_page
        pages = (pages + 1) if num_film_locations % results_per_page > 0 else pages

        prev = 0
        if (page + 1) <= pages:
            next = page + 1
        else:
            next = 0
        if (page - 1) > 0:
            prev = page - 1

        return {
            'prev' : prev,
            'next' : next,
            'current' : page,
            'count' : num_film_locations,
            'pages' : pages
        }