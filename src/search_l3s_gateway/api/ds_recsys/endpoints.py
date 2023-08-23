## import libraries
from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
import requests, json
import os, socket



ns_ds_recsys = Namespace("ds-recsys", validate=True, description="downstream endpoints for recsys services")


@ns_ds_recsys.route('/recsys-service/ok', endpoint="recsys_service_ok")
class RecommendationService(Resource):
    @ns_ds_recsys.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_ds_recsys.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_ds_recsys.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_ds_recsys.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def get(self):
        return {"message": "success"}, HTTPStatus.OK