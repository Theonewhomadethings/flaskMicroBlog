from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

'''
This script creates the application object as an instance of class Flask imported from the flask package
'''

#the name variable passed to the flask class is a python predefined variable, which is set to the name of the module in which it is used.
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
#the routes module is imported at the bottom on purpose not on the top of the script.
#the bottom import is a workaround to circular imports, a problem with flask apps
#the routes module needs to impor the app variable defined in this script
