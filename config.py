import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    REDIS_AUTOCOMPLETE_SORTED_SET = 'locations'
    RESULTS_PER_PAGE = 10
    REDIS_HOSTNAME = 'localhost'
    REDIS_PORT = 11827
    REDIS_DB = 0
    REDIS_PASSWORD = None

class TestingConfig(Config):
    TESTING = True
    REDIS_AUTOCOMPLETE_SORTED_SET = 'locations'
    RESULTS_PER_PAGE = 10
    REDIS_HOSTNAME = 'localhost'
    REDIS_PORT = 11827
    REDIS_DB = 0
    REDIS_PASSWORD = None

class ProductionConfig(Config):
    PRODUCTION = True
    REDIS_AUTOCOMPLETE_SORTED_SET = 'locations'
    RESULTS_PER_PAGE = 10

class HerokuConfig(Config):
    HEROKU = True
    REDIS_AUTOCOMPLETE_SORTED_SET = 'locations'
    RESULTS_PER_PAGE = 10
    REDIS_HOSTNAME = 'barreleye.redistogo.com'
    REDIS_PORT = 11827
    REDIS_DB = 0
    REDIS_PASSWORD = '5699e9d4926920a4df64d264871c05de'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'default': DevelopmentConfig
}
