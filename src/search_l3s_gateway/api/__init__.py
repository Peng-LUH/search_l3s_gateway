"""API blueprint configuration"""
from flask import Blueprint
from flask_restx import Api

from search_l3s_gateway.api.upstream.endpoints import ns_upstream
from search_l3s_gateway.api.downstream.endpoints import ns_downstream
# from search_l3s_gateway.api.search_srv import ns_search

api_bp = Blueprint("api", __name__, url_prefix="/l3s-gateway")
# authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}


api = Api(api_bp,
          version="0.0.1",
          title="L3S Gateway for SEARCH",
          description="Welcome to the Swagger UI documentation site!",
          # doc="/l3s-gateway",
          # authorizations=authorizations,
          )

api.add_namespace(ns_upstream, path="/upstream")
api.add_namespace(ns_downstream, path="/downstream")
