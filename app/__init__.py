from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy

#initialize the application
app = Flask(__name__)

#set up the configuration
app.config.from_object(DevConfig)
#app.config.from_pyfile("config.py")

#initialize flask extensions
bootstrap.init_app(app)
db.init_app(app)

from app import views
