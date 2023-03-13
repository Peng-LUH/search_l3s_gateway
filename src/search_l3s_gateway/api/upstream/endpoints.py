from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus



ns_upstream = Namespace("upstream", validate=True)


todo = ns_upstream.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

@ns_upstream.route("/test_upstream", endpoint="test_upstream")
class TestUpstream(Resource):
    def get(self):
        return {"message": "get method from test upstream endpoint."}, HTTPStatus.OK
    
    @ns_upstream.expect(todo)
    def post(self):
        data = ns_upstream.payload
        return data, HTTPStatus.CREATED