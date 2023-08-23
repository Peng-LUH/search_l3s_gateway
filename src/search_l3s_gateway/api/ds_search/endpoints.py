from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
import requests, json
import os, socket


# from search_l3s_gateway.api import api
from .dto import (
    search_srv_request_model,
    recsys_srv_request_model
    )


ns_ds_search = Namespace("ds-search", validate=True, description="downstream endpoints for search services")

ns_ds_search.models[search_srv_request_model.name] = search_srv_request_model
ns_ds_search.models[recsys_srv_request_model.name] = recsys_srv_request_model


@ns_ds_search.route('/search-service/ok', endpoint="search_service_ok")
class SearchServiceOK(Resource):
    @ns_ds_search.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_ds_search.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_ds_search.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_ds_search.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def get(self):
        url = f'http://{os.getenv("HOST_IP")}:{os.getenv("L3S_SEARCH_PORT")}'
        # url = f'http://{os.getenv("HOST_IP")}:{os.getenv(port)}'
        
        result = {}
        try:
            response = requests.head(url)
            if response.status_code == 200:
                return result.update({"l3s-search": 'success'}), HTTPStatus.OK
            else:
                return result.update({"l3s-search": 'failed'}), HTTPStatus.INTERNAL_SERVER_ERROR
        except requests.ConnectionError as e:
            result.update({"l3s-search": e.errno})
            return result, HTTPStatus.NOT_FOUND
    


@ns_ds_search.route('/search-service/datasets', endpoint="search_service_datasets")
class SearchServiceDatasets(Resource):
    @ns_ds_search.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_ds_search.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_ds_search.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_ds_search.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def get(self):
        """get the name of datasets as list"""
        url = f'http://{os.getenv("HOST_IP")}:{os.getenv("L3S_SEARCH_PORT")}/l3s-search/search-metadata/get-datasets'
        # headers = {
        #     'accept': 'application/json',
        #     'Content-Type': 'application/json'
        # }
        response = requests.get(url)
        return response.json()
     

### Connection: search services
@ns_ds_search.route('/search-service/dense-retrieval', endpoint="search_service")
class SearchService(Resource):
    @ns_ds_search.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_ds_search.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_ds_search.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_ds_search.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    @ns_ds_search.expect(search_srv_request_model)
    def post(self):
        # current_ip = os.getenv("HOST_IP")
        l3s_search_port = os.getenv("L3S_SEARCH_PORT")
        url = f'http://{os.getenv("HOST_IP")}:{os.getenv("L3S_SEARCH_PORT")}/l3s-search/searcher/dense-retrieval'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        data = ns_ds_search.payload
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        return response.json()
    


# @ns_ds_search.route('/search_service/add-new-nugget', endpoint="add_new_nugget")
# class 