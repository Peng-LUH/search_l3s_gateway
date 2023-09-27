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

SEARCH_BASE_URL = f'http://{os.getenv("HOST_IP")}:{os.getenv("L3S_SEARCH_PORT")}'

@ns_ds_search.route('/search-service/ok', endpoint="search_service_ok")
class SearchServiceOK(Resource):
    @ns_ds_search.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_ds_search.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_ds_search.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_ds_search.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def get(self):
        # url = f'http://{os.getenv("HOST_IP")}:{os.getenv("L3S_SEARCH_PORT")}'
        url = SEARCH_BASE_URL
        
        result = {}
        try:
            response = requests.head(url)
            if response.status_code == 200:
                result.update({"l3s-search": 'success'})
                return result, HTTPStatus.OK
            else:
                result.update({"l3s-search": 'failed'})
                return result, HTTPStatus.INTERNAL_SERVER_ERROR
        except requests.ConnectionError as e:
            result.update({"l3s-search": e.strerror})
            return result, HTTPStatus.NOT_FOUND
        
        # return {"URL": requests.head(url).status_code}, HTTPStatus.OK
    


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
     
@ns_ds_search.route('search-service/meta-datasets')
class SearchServiceMetaDatasets(Resource):
    @ns_ds_search.response(int(HTTPStatus.OK), "get successfully.")
    @ns_ds_search.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_ds_search.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_ds_search.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_ds_search.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def get(self):
        url = f"{SEARCH_BASE_URL}/l3s-search/search-metadata/get-datasets"
        print(url)
        try:
            response = requests.get(url)
            print(response.status_code)
            # print(response.json())
            if response.status_code == 200:
                return response.json(), HTTPStatus.OK
            if response.status_code == 404:
                return {"Error": "l3s-search service not found"}, HTTPStatus.NOT_FOUND
        except requests.ConnectionError as e:
            return {"Error": e.strerror}, HTTPStatus.BAD_REQUEST





from flask import jsonify, request
from swagger_client_L3S import l3s_search_client
# from swagger_client_L3S import l3s_recsys_client as l3SSearchClient
import dataclasses, json
from pprint import pprint
from swagger_client_L3S.l3s_search_client.rest import ApiException
import os

from swagger_client_L3S.l3s_search_client.models.dense_search_response import DenseSearchResponse
from swagger_client_L3S.l3s_search_client.models.dense_search_request import DenseSearchRequest
from swagger_client_L3S.l3s_search_client.models.dense_search_response_list import DenseSearchResponseList
# from swagger_client_L3S.l3s_search_client.models.random_response import RandomResponse
# from swagger_client_L3S.l3s_search_client.models.random_request import RandomRequest

## Configuration L3S Recsys
l3s_search_config = l3s_search_client.Configuration()
# l3s_search_config.host = "http://localhost:9043/l3s-search"
l3s_search_config.host = os.getenv('L3S_SEARCH_HOST')
print(l3s_search_config.host)


client_l3s_search = l3s_search_client.ApiClient(configuration=l3s_search_config)
# l3s recsys api registration
search_searcher_api = l3s_search_client.SearcherApi(api_client=client_l3s_search)
# recsys_random_api = l3s_search_client.RandomApi(api_client=client_l3s_search)


from flask_restx import reqparse
parser = reqparse.RequestParser()
parser.add_argument('uid', type=str, location='args', default='None')
parser.add_argument('cid', type=str, location='args', default='None')
parser.add_argument('query', type=str, required=True, location='args')
parser.add_argument('nresults', type=int, location='args', default=10)

### Connection: search services
@ns_ds_search.route('/dense-retrieval', endpoint="dense_retrieval")
class SearchService(Resource):
    @ns_ds_search.expect(parser)
    def get(self):
        # current_ip = os.getenv("HOST_IP")
        # l3s_search_port = os.getenv("L3S_SEARCH_PORT")
        # url = f'http://{os.getenv("HOST_IP")}:{os.getenv("L3S_SEARCH_PORT")}/l3s-search/searcher/dense-retrieval'
        # headers = {
        #     'accept': 'application/json',
        #     'Content-Type': 'application/json'
        # }
        # data = ns_ds_search.payload
        # response = requests.post(url, headers=headers, data=json.dumps(data))
        
        # return response.json()
        args=parser.parse_args()
        print(type(args))
        
        if args.get('uid') == 'None':
            uid = ""
        if args.get('cid') == 'None':
            cid = ""
            
        request_data = {
                        "uid": uid,
                        "cid": cid,
                        "query": args.get('query'),
                        "language_model": "bert-base-german-cased",
                        "index_method": "flat-l2",
                        "dataset_name": "mls-tasks",
                        "nr_result": args.get('nresults')
                        }
        
        pprint(request_data)
        
        try:
            print(search_searcher_api.api_client.configuration.host)
            api_response = search_searcher_api.post_dense_retrieval(body=request_data)
        
            print(api_response)
            pprint(api_response)
            
            d = DenseSearchResponseList(results=api_response.results)
            response = jsonify(d.to_dict())
            response.status_code = 201
            return response
        except ApiException as e:
       
            return ("Exception when calling Api-> %s\n" % e)
        
        # return request_data
    

# @ns_ds_search.route('/search_service/add-new-nugget', endpoint="add_new_nugget")
# class 