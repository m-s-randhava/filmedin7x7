__author__ = 'mohanrandhava'

from flask.ext.restful import Resource, reqparse
from app.storage.redis import RedisStore, RedisException
from flask import current_app, request, Response, abort
import urllib
import json

"""
REST API ENDPOINT: FilmsAtLocations

PROVIDES all films which fully and/or partially match word prefix(es)
or phrases.  The results are a json list of all matching films' full
metadata.

    ->  IF a 'single-word' (a single letter, a prefix, or whole word)
        is presented, a match will be attempted against all candidates
        where the 'Locations' entry has a word with any prefix matching
        that 'single-word.'
    ->  IF multiple 'single-words' are presented, a match will be attempted
        against all candidates where the 'Locations' entry has words, where
        a subset exists with prefixes matching all 'single-words' provided.
"""
class FilmsAtLocations(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(FilmsAtLocations, self).__init__()

    def get(self, location):
        """
        :param - location
            The actual word prefix, whole word or words, comprising
            Location search phrase.
        :queryparam - ac_selected
            Whether or not user selected the Location via the autocomplete
            result dropdown or from typed entry.  If the former an exact
            match is made to the chosen Location, else a partial match
            is made.
        :queryparam - page
            Which page of paginated results to show

        RETURNS list of json results with each entry comprising full film
        metadata.  Pagination information is sent via headers:
            prev    -   previous page to current, 0 if none
            next    -   next page to current, 0 if none
            page    -   current requested page
            num_films_at_locations  - total number of films 'matching' location
            pages   - number of pages of results, 10 per page
        """
        p = request.args.get('page')
        ac = request.args.get('ac_selected')

        if p is None:
            abort(400)

        page = int(p)

        location = urllib.unquote(location).decode('utf8')

        try:
            r_store = RedisStore(current_app.config['REDIS_AUTOCOMPLETE_SORTED_SET'], current_app.config['REDIS_HOSTNAME'], current_app.config['REDIS_PORT'], current_app.config['REDIS_DB'], current_app.config['REDIS_PASSWORD'])
            film_locations = r_store.search(location)
        except RedisException:
            print "Redis unavailable ..."
            response = Response('[]', status=200, mimetype='application/json')
            response.headers['prev'] = 0
            response.headers['next'] = 0
            response.headers['page'] = page
            response.headers['num_films_at_locations'] = 0
            response.headers['pages'] = 0

            return response

        if ac is not None and ac == 'True':
            film_locations = [film_location for film_location in film_locations if film_location['Locations'] == location]

        num_films_at_locations = len(film_locations)

        start = 10 * (page - 1)
        end = (start + 10) if (start + 10) < num_films_at_locations else num_films_at_locations

        results_per_page = current_app.config['RESULTS_PER_PAGE']

        pages = num_films_at_locations/results_per_page
        pages = (pages + 1) if num_films_at_locations % results_per_page > 0 else pages

        prev = 0
        if (page + 1) <= pages:
            next = page + 1
        else:
            next = 0
        if (page - 1) > 0:
            prev = page - 1

        js = json.dumps(film_locations[start:end])

        response = Response(js, status=200, mimetype='application/json')

        response.headers['prev'] = prev
        response.headers['next'] = next
        response.headers['page'] = page
        response.headers['num_films_at_locations'] = num_films_at_locations
        response.headers['pages'] = pages

        return response