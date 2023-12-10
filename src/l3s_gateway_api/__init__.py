"""Flask app initialization via factory pattern."""

from flask import Flask, redirect, request
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from l3s_gateway_api.config import get_config

import os, socket


cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
ma = Marshmallow()




def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    os.environ["API_BASE_PATH"] = os.getcwd()
    
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    
    @app.route("/")
    def index():
        # print(request.host_url)
        return redirect(f'{request.host_url}l3s-gateway/', code=200)
    
    # to avoid a circular import
    from l3s_gateway_api.api import api_bp

    app.register_blueprint(api_bp)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    ma.init_app(app)
    
    return app
