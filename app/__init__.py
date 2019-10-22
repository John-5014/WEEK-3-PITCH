from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy   

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
  app = Flask(__name__)

  app.config.from_object(config_options[config_name])

  #initializing flask extensions
  from .auth import auth as auth_blueprint

  app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
  bootstrap.init_app(app)
  db.init_app(app)
   
  return app
      