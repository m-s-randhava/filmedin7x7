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

class TestingConfig(Config):
    TESTING = True
    REDIS_AUTOCOMPLETE_SORTED_SET = 'locations'
    RESULTS_PER_PAGE = 10

class ProductionConfig(Config):
    PRODUCTION = True
    REDIS_AUTOCOMPLETE_SORTED_SET = 'locations'
    RESULTS_PER_PAGE = 10

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
