import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))

with open('./critical_flie/databaseAccount.json') as accountReader:
    dbAccount = json.loads(accountReader.read())

DB_URL = """mysql+pymysql://%s:%s@%s/stocker?charset=utf8""" % (
        dbAccount["username"], dbAccount["password"], dbAccount["ip"])

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess db.String'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_SLOW_DB_QUERY_TIME = 0.5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or DB_URL


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or DB_URL


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

