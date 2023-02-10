'''
This is a configuration class in a seperate python module. 
keep in top-level directory
we are going to use a class to store configuration variables.

'''
import os 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' #cryptographic key, to generate signatures or tokens
    SQLALCHEMY_DATABASE_URI  = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db' )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


