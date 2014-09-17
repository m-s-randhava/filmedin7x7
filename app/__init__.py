from flask import Flask
from flask.ext.restful import Api
from flask.ext.bootstrap import Bootstrap
from config import config
from main import allFilmLocations, FilmLocationsAPI, FilmLocationsPaginationAPI, AutocompleteAPI
from app.migration import loadRedis

bootstrap = Bootstrap()
api = Api()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    api.init_app(app)

    app.route('/',)
    api.add_resource(allFilmLocations.TaskListAPI, '/todo/api/v1.0/tasks', endpoint = 'tasks')
    api.add_resource(AutocompleteAPI.AutoCompleteLocation, '/film/locations/autocomplete', endpoint = 'filmlocations_auto_complete')
    api.add_resource(FilmLocationsAPI.FilmLocations, '/film/locations/<string:location>', endpoint = 'film_locations')
    api.add_resource(FilmLocationsPaginationAPI.FilmLocationsPagination, '/film/locations/pagination/<string:location>', endpoint = 'film_locations_pagination')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def setup_app(config_name):
    l = loadRedis.LoadRedis(config_name, 'film_locations_in_san_francisco_decorated.json', 'film_locations_in_san_francisco_coord.json')
    l.load_locations_prefixes_into_redis()
    return
