from os import environ

class Config:
     SQLALCHEMY_DATABASE_URI = environ.get('DB_URI')
     SQLALCHEMY_TRACK_MODIFICATIONS = False