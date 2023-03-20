from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
from flask_restx.reqparse import RequestParser

from search_l3s_gateway import db
from search_l3s_gateway.models.user import User
from search_l3s_gateway.api.upstream.dto import service_reqparser


ns_upstream = Namespace("upstream", validate=True)

request_model = ns_upstream.model('Request', {
    'user_id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

todo_parser = RequestParser()
todo_parser.add_argument(name="id", type=str, location="form")


@ns_upstream.route("/test_upstream", endpoint="test_upstream")
class TestUpstream(Resource):
    def get(self):
        return {"message": "get method from test upstream endpoint."}, HTTPStatus.OK

    @ns_upstream.expect(todo_parser)
    def post(self):
        data = todo_parser.parse_args()
        return data, HTTPStatus.CREATED


@ns_upstream.route("/service-request", endpoint="service_request")
class ServiceRequest(Resource):
    @ns_upstream.expect(service_reqparser)
    @ns_upstream.response(int(HTTPStatus.CREATED), "request accepted")
    def post(self):
        request_data = service_reqparser.parse_args()
        # request_data.headers['Content-Type'] = "application/json"
        # check if company exists, if not create
        user_id = request_data.get("user_id")
        if user_id:
            user = db.session.execute(db.select(User).filter_by(user_id=user_id)).first()
            if user:
                user = user[0]
            else:
                new_user = User(user_id = user_id)
        # check if user exists, if not create
        
        return request_data


@ns_upstream.route("/retrieve-info", endpoint="retrieve_info")
class RetrieveInfo(Resource):
    def post(self):
        pass