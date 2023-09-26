"""API blueprint configuration"""
from flask import Blueprint
from flask_restx import Api

from l3s_gateway_api.api.upstream.endpoints import ns_upstream
from l3s_gateway_api.api.downstream.endpoints import ns_downstream
from l3s_gateway_api.api.search_srv.endpoints import ns_ds_search
from l3s_gateway_api.api.recsys_srv.endpoints import ns_recsys_srv
from l3s_gateway_api.api.aimeta_srv.endpoints import ns_ds_aimeta
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


# namespace resgistration
# api.add_namespace(ns_upstream, path="/upstream")
# api.add_namespace(ns_downstream, path="/downstream")
api.add_namespace(ns_ds_search, path="/l3s-search")
api.add_namespace(ns_recsys_srv, path="/l3s-recsys")
api.add_namespace(ns_ds_aimeta, path="/l3s-aimeta")
