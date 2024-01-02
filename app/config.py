from datetime import timedelta
class Constants(object):
    Debug = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///FlaskDatabase.db'
    JWT_SECRET_KEY = 'SECT_KEY'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(45)
    

class Developement(Constants):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'SECRET_KEY_DEV'
    INPUT_FOLDER = './static'
    OUTPUT_FOLDER='./output'
class Production(Constants):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'SECRET_KEY_PROD'
    INPUT_FOLDER = '/static'
    OUTPUT_FOLDER='/output'
