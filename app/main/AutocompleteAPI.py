__author__ = 'mohanrandhava'

from flask.ext.restful import Resource, reqparse
from app.storage.redis import RedisStore
from flask import current_app, request

class AutoCompleteLocation(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(AutoCompleteLocation, self).__init__()

    def get(self):
        search_term = request.args.get('term')
        rStore = RedisStore(current_app.config['REDIS_AUTOCOMPLETE_SORTED_SET'])
        rStoreResults = rStore.search(search_term)
        response = [rStoreResult['Locations'] for rStoreResult in rStoreResults]
        return response