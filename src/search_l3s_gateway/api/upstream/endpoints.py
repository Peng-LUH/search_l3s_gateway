from http import HTTPStatus

# import flask
from flask import request, url_for, make_response, jsonify

# import flask-restx
from flask_restx import Namespace, Resource, fields
from flask_restx.reqparse import RequestParser

# import .
from search_l3s_gateway import db
from search_l3s_gateway.models.user import User
from search_l3s_gateway.api.upstream import ns_upstream


## import flask-restx-model
from search_l3s_gateway.api.upstream.dto import (
    test_model,
    service_model,
    request_model,
    retrieve_model
)

@ns_upstream.route("/test_upstream", endpoint="test_upstream")
class TestUpstream(Resource):
    def get(self):
        return {"message": "get method from test upstream endpoint."}, HTTPStatus.OK

    @ns_upstream.expect(test_model)
    def post(self):
        data = request.json()
        return data, HTTPStatus.CREATED


@ns_upstream.route("/service-request", endpoint="service_request")
class ServiceRequest(Resource):
    @ns_upstream.expect(service_model)
    @ns_upstream.response(int(HTTPStatus.CREATED), "request accepted")
    def post(self):
        request_data = request.json()
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
    @ns_upstream.expect(retrieve_model)
    def post(self):
        pass
    
    
@ns_upstream.route("/get-users", endpoint="get_users")
class GetUsers(Resource):
    def get(self):
        try:
            users = User.query.all()
            return make_response(jsonify([user.json() for user in users]), 200)
        except:
            return make_response(jsonify({'message': 'error getting users'}), 500)