from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

# from search_l3s_gateway.api import api

ns_downstream = Namespace("downstream", validate=True)

todo = ns_downstream.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

@ns_downstream.route("/test_downstream", endpoint="test_downstream")
class TestUpstream(Resource):
    @ns_downstream.response(int(HTTPStatus.CREATED), "successfully get.")
    @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def get(self):
        return {"message": "get method from test downstream endpoint."}, HTTPStatus.OK
    
    
    @ns_downstream.response(int(HTTPStatus.CREATED), "successfully created.")
    @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    @ns_downstream.expect(todo)
    def post(self):
        data = ns_downstream.payload
        return data, HTTPStatus.CREATED
    
    
    @ns_downstream.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    @ns_downstream.expect(todo)
    def put(self):
        data = ns_downstream.payload
        return data, HTTPStatus.ACCEPTED
    
    
    @ns_downstream.response(int(HTTPStatus.CREATED), "successfully deleted.")
    @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def delete(self):
        return {"message": "delete method downstream"}, HTTPStatus.OK