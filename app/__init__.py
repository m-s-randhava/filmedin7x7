from flask import Flask
from flask.ext.restful import Api
from flask.ext.bootstrap import Bootstrap
from config import config
from main import FilmsAtLocationsAPI, AutocompleteAPI, FindNearestFilmsAtLocationAPI
from app.migration import LoadRedisWithLocationPrefixes

bootstrap = Bootstrap()
api = Api()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    api.init_app(app)

    app.route('/',)
    api.add_resource(AutocompleteAPI.AutoCompleteLocation, '/film/locations/autocomplete', endpoint = 'filmlocations_auto_complete')
    api.add_resource(FilmsAtLocationsAPI.FilmsAtLocations, '/film/locations/<string:location>', endpoint = 'film_locations')
    api.add_resource(FindNearestFilmsAtLocationAPI.FindNearest7FilmsAtLocation, '/film/7nearme/lat/<float:lat>/<string:lat_sign>/lng/<float:lng>/<string:lng_sign>', endpoint = 'films_near_me')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def setup_app(config_name):
    l = LoadRedisWithLocationPrefixes.LoadRedisWithLocationPrefixes(config_name, 'film_locations_in_san_francisco_decorated.json', 'film_locations_in_san_francisco_coord.json')
    l.load_locations_prefixes_into_redis()
    return
