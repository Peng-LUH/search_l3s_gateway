"""gateway for search service from l3s"""

from http import HTTPStatus
from flask_restx import Namespace, Resource
from search_l3s_gateway import db
# from flask_api_tutorial.models.user import User
# from flask_api_tutorial.api.auth.dto import auth_regparser
# from flask_api_tutorial.api.auth.business import process_registration_request

ns_search = Namespace(name="search_gateway", validate=True)


@ns_search.route("/search_srv")

def get(self):
    pass

def post(self):
    pass

def put(self):
    pass


