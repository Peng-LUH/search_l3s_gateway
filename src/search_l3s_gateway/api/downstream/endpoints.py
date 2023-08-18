# from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
import requests, json

# from search_l3s_gateway.api import api
from .dto import (
    todo,
    search_srv_request_model,
    recsys_srv_request_model
    )

ns_downstream = Namespace("downstream", validate=True)

# register dto models
ns_downstream.models[search_srv_request_model.name] = search_srv_request_model
ns_downstream.models[recsys_srv_request_model.name] = recsys_srv_request_model
ns_downstream.models[todo.name] = todo

# @ns_downstream.route("/test_downstream", endpoint="test_downstream")
# class TestUpstream(Resource):
#     @ns_downstream.response(int(HTTPStatus.CREATED), "successfully get.")
#     @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
#     @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
#     @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
#     def get(self):
#         return {"message": "get method from test downstream endpoint."}, HTTPStatus.OK

#     @ns_downstream.response(int(HTTPStatus.CREATED), "successfully created.")
#     @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
#     @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
#     @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
#     @ns_downstream.expect(todo)
#     def post(self):
#         data = ns_downstream.payload
#         return data, HTTPStatus.CREATED

#     @ns_downstream.response(int(HTTPStatus.CREATED), "successfully changed.")
#     @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
#     @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
#     @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
#     @ns_downstream.expect(todo)
#     def put(self):
#         data = ns_downstream.payload
#         return data, HTTPStatus.ACCEPTED

#     @ns_downstream.response(int(HTTPStatus.CREATED), "successfully deleted.")
#     @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
#     @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
#     @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
#     def delete(self):
#         return {"message": "delete method downstream"}, HTTPStatus.OK


### Connection: search services
@ns_downstream.route('/search-service', endpoint="search_service")
class SearchService(Resource):
    @ns_downstream.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    @ns_downstream.expect(search_srv_request_model)
    def post(self):
        url = 'http://127.0.0.1:5001/api/v1/searcher/dense-retrieval'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        data = ns_downstream.payload
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        return response.json()
    

### Connection: recommendation service
@ns_downstream.route('/recsys-service', endpoint="recsys_service")
class RecommendationService(Resource):
    @ns_downstream.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    @ns_downstream.expect(recsys_srv_request_model)
    def post(self):
        url = 'http://127.0.0.1:5002/api/v1/searcher/dense-retrieval'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        data = ns_downstream.payload
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        return response.json()
    

### Connection: question generation service
@ns_downstream.route('/ai-meta-service', endpoint="ai_meta_service")
class QGenService(Resource):
    @ns_downstream.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    @ns_downstream.expect(todo)
    def post(self):
        pass
    

# ### Connection: summary service
# @ns_downstream.route('/summary-service', endpoint="summary_service")
# class SummaryService(Resource):
#     @ns_downstream.response(int(HTTPStatus.CREATED), "successfully changed.")
#     @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
#     @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
#     @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
#     @ns_downstream.expect(todo)
#     def post(self):
#         pass
    

