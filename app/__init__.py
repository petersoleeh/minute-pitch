from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initialize the application
app = Flask(__name__)

#set up the configuration
app.config.from_object(DevConfig)
#app.config.from_pyfile("config.py")

#initialize Bootstrap
bootstrap = Bootstrap(app)

from app import views
