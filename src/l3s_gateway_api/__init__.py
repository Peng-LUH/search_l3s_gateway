"""Flask app initialization via factory pattern."""

from flask import Flask, redirect
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from l3s_gateway_api.config import get_config

import os, socket


cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))


    # os.environ["HOST"] = socket.gethostname()
    # os.environ["HOST_IP"] = socket.gethostbyname(os.getenv("HOST_NAME"))
    # os.environ["HOST_IP"] = "localhost"
    
    
    @app.route("/")
    def index():
        return redirect(f'http://{os.getenv("HOST_IP")}:{os.getenv("L3S_GATEWAY_PORT")}/l3s-gateway/', code=200)
    
    # to avoid a circular import
    from l3s_gateway_api.api import api_bp

    app.register_blueprint(api_bp)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    
    
    return app
