__author__ = 'mohanrandhava'

import sys
from flask.ext.restful import Resource, reqparse
from app.storage.redis import RedisStore, RedisException
from flask import current_app, request

"""
REST API ENDPOINT: AutoCompletion

PROVIDES autocompletion results for any incoming phrase, from a
single-letter to multi-word phrase.  The results are a list of
matching Location strings.

    ->  IF a 'single-word' (a single letter, a prefix, or whole word)
        is presented, a match will be attempted against all candidates
        where the 'Locations' entry has a word with any prefix matching
        that 'single-word.'
    ->  IF multiple 'single-words' are presented, a match will be attempted
        against all candidates where the 'Locations' entry has words, where
        a subset exists with prefixes matching all 'single-words' provided.
"""

class AutoCompleteLocation(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(AutoCompleteLocation, self).__init__()

    def get(self):
        """
        :queryparam - term
            Word prefix, whole word, or phrase that is passed in an queried upon

        RETURNS list of results
        """
        search_term = request.args.get('term')
        response = []

        #   Wrap access to Redis in try/catch to insure against unavailability for any reason
        try:
            rStore = RedisStore(current_app.config['REDIS_AUTOCOMPLETE_SORTED_SET'], current_app.config['REDIS_HOSTNAME'], current_app.config['REDIS_PORT'], current_app.config['REDIS_DB'], current_app.config['REDIS_PASSWORD'])
            rStoreResults = rStore.search(search_term)
            response = [rStoreResult['Locations'] for rStoreResult in rStoreResults]
        except RedisException:
            print "Redis unavailable ..."

        return response