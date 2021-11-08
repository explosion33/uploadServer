import os
from random import randint

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET KEY' # Prevents CSRF attacks
    PORT = os.getenv("PORT")
    ROOT = os.path.dirname(os.path.abspath(__file__))