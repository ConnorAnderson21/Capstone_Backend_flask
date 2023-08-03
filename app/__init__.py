from flask import Flask
from flask_migrate import Migrate
from config import Config
from .models import db, User
from flask_cors import CORS
from .api.routes import api

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
CORS(app)

migrate = Migrate(app, db)

app.register_blueprint(api)

from . import routes
from . import models
