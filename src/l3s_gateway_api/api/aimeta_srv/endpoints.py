## import libraries
from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
import requests, json
import os, socket


# create namespace
ns_ds_aimeta = Namespace("ds-aimeta", validate=True, description="downstream endpoints for aimeta services")




### Connection: question generation service
@ns_ds_aimeta.route('/aimeta-service/ok', endpoint="aimeta_service_ok")
class AiMetaOk(Resource):
    @ns_ds_aimeta.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_ds_aimeta.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_ds_aimeta.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_ds_aimeta.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def get(self):
        return {"message": "success"}, HTTPStatus.OK