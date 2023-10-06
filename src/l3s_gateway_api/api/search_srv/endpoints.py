import os, socket, requests, json, dataclasses
from pprint import pprint
from http import HTTPStatus


from flask import request, jsonify, url_for, current_app
from flask_restx import Namespace, Resource, fields


## ------------ config: l3s_search_client --------------- ##
from swagger_client_L3S import l3s_search_client
l3s_search_config = l3s_search_client.Configuration()
l3s_search_config.host = "http://localhost:9043/l3s-search"
# l3s_search_config.host = os.getenv('L3S_SEARCH_HOST')
print("*"*80)
print("l3s-search-service-host: ", l3s_search_config.host)
print("*"*80)

client_l3s_search = l3s_search_client.ApiClient(configuration=l3s_search_config)
# l3s recsys api registration
search_searcher_api = l3s_search_client.SearcherApi(api_client=client_l3s_search)
# recsys_random_api = l3s_search_client.RandomApi(api_client=client_l3s_search)
search_metadata_api = l3s_search_client.MetadataApi(api_client=client_l3s_search)


## ----------------- import dtos from l3s_search_client ----------------- ##
from swagger_client_L3S.l3s_search_client.rest import ApiException
from swagger_client_L3S.l3s_search_client.models.dto_dense_search_request import DtoDenseSearchRequest
from swagger_client_L3S.l3s_search_client.models.dto_dense_search_response import DtoDenseSearchResponse
from swagger_client_L3S.l3s_search_client.models.dto_dense_search_response_list import DtoDenseSearchResponseList
from swagger_client_L3S.l3s_search_client.models.dto_dataset_list import DtoDatasetList
from swagger_client_L3S.l3s_search_client.models.dto_encode_type_list import DtoEncodeTypeList

ns_search_srv = Namespace("Search Service", validate=True, description="downstream endpoints for search services")


# SEARCH_BASE_URL = f'http://{os.getenv("HOST_IP")}:{os.getenv("L3S_SEARCH_PORT")}'
# with current_app.request_context():
#     print(request.host_url)

@ns_search_srv.route('/test', endpoint='test')
class Test(Resource):
    def get(self):
        print(request.host_url)
        print(url_for('api.search_service_ok'))
        return {"results": f"{url_for('api.search_service_ok')}"}


# from search_l3s_gateway.api import api
from .dto import search_srv_request_model, recsys_srv_request_model
ns_search_srv.models[search_srv_request_model.name] = search_srv_request_model
ns_search_srv.models[recsys_srv_request_model.name] = recsys_srv_request_model



from .dto import model_search_srv_connection_response
ns_search_srv.models[model_search_srv_connection_response.name] = model_search_srv_connection_response

@ns_search_srv.route('/connection', endpoint="search_srv_connection")
class SearchServiceOK(Resource):
    @ns_search_srv.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_search_srv.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_search_srv.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_search_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    @ns_search_srv.marshal_with(model_search_srv_connection_response)
    def get(self):
        # url = os.getenv('L3S_SEARCH_HOST')+'/'
        url = l3s_search_config.host+'/'
        print(url)
        # print(url_for(search_service_ok))
        result = {}
        try:
            response = requests.head(url)
            if response.status_code == 200:
                result.update({"host_url": url, "status": 'success'})
                return result, HTTPStatus.OK
            else:
                result.update({"host_url": url, "status": 'failed'})
                return result, HTTPStatus.INTERNAL_SERVER_ERROR
        except requests.ConnectionError as e:
            result = {"host_url": url}
            result.update({"connection": e.strerror})
            return result, HTTPStatus.NOT_FOUND
        
        # return {"URL": requests.head(url).status_code}, HTTPStatus.OK
    

## ------------------- dataset ------------------ ##
from .dto import model_get_dataset_response
ns_search_srv.models[model_get_dataset_response.name] = model_get_dataset_response
@ns_search_srv.route('/datasets', endpoint="search_service_datasets")
class SearchServiceDatasets(Resource):
    @ns_search_srv.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_search_srv.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_search_srv.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_search_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    @ns_search_srv.marshal_with(model_get_dataset_response)
    def get(self):
        """get the name of datasets as list"""
        url = f'{os.getenv("L3S_SEARCH_HOST")}/search-metadata/get-datasets'
        
        api_response = search_metadata_api.get_get_datasets()
        print(type(api_response))
        # pprint(api_response)
        
        response_data = DtoDatasetList(results=api_response.results).to_dict()
        # response = jsonify(d.to_dict())
        # print(response_data["results"])
        # for r in response_data["results"]:
        #     print(r)
        datasets = []
        for r in response_data["results"]:
            datasets.append(r["name"])   
        
        
        response = {"results": datasets}
        return response, HTTPStatus.OK

    def post(self):
        """create a new dataset"""
        pass
    
    def put(self):
        """update a dataset"""
        pass


@ns_search_srv.route('/encode-type', endpoint="get_encode_type")
class SearchServiceDatasets(Resource):
    @ns_search_srv.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_search_srv.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_search_srv.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_search_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def get(self):
        """get the name of encoding types as list"""
        url = f'{os.getenv("L3S_SEARCH_HOST")}/search-metadata/get-datasets'
        
        api_response = search_metadata_api.get_get_encoding_type()
        print(type(api_response))
        # pprint(api_response)
        
        d = DtoEncodeTypeList(results=api_response.results)
        response = jsonify(d.to_dict())
        response.status_code = 201
        # response = requests.get(url)
        return response
    
# @ns_search_srv.route('search-service/meta-datasets')
# class SearchServiceMetaDatasets(Resource):
#     @ns_search_srv.response(int(HTTPStatus.OK), "get successfully.")
#     @ns_search_srv.response(int(HTTPStatus.CREATED), "successfully changed.")
#     @ns_search_srv.response(int(HTTPStatus.CONFLICT), "exits conflict.")
#     @ns_search_srv.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
#     @ns_search_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
#     def get(self):
#         url = f"{SEARCH_BASE_URL}/l3s-search/search-metadata/get-datasets"
#         print(url)
#         try:
#             response = requests.get(url)
#             print(response.status_code)
#             # print(response.json())
#             if response.status_code == 200:
#                 return response.json(), HTTPStatus.OK
#             if response.status_code == 404:
#                 return {"Error": "l3s-search service not found"}, HTTPStatus.NOT_FOUND
#         except requests.ConnectionError as e:
#             return {"Error": e.strerror}, HTTPStatus.BAD_REQUEST



from flask_restx import reqparse
parser_search_user = reqparse.RequestParser()
# parser.add_argument('user_id', type=str, location='args', default='None')
parser_search_user.add_argument('owner', type=str, location='args', default='None')
parser_search_user.add_argument('query', type=str, required=True, location='args', default='Elektrotechnik 1 Versuch 8: Wirkleistung von Wechselspannungen; Wirkleistung der Sinuswechselspannung in der praktischen Übung')
parser_search_user.add_argument('num_results', type=int, location='args', default=10)

### Connection: search services
@ns_search_srv.route('/search/<string:user_id>', endpoint="search_user")
class SearchService(Resource):
    @ns_search_srv.expect(parser_search_user)
    def get(self, user_id):
        # current_ip = os.getenv("HOST_IP")
        # l3s_search_port = os.getenv("L3S_SEARCH_PORT")
        # url = f'http://{os.getenv("HOST_IP")}:{os.getenv("L3S_SEARCH_PORT")}/l3s-search/searcher/dense-retrieval'
        # headers = {
        #     'accept': 'application/json',
        #     'Content-Type': 'application/json'
        # }
        # data = ns_search_srv.payload
        # response = requests.post(url, headers=headers, data=json.dumps(data))
        
        # return response.json()
        args=parser_search_user.parse_args()
        pprint(args)
        
        if args.get('owner') == 'None':
            owner = ""
            
        request_data = {
                        "user_id": user_id,
                        "owner": owner,
                        "query": args.get('query'),
                        "language_model": "bert-base-german-cased",
                        "index_method": "flat-l2",
                        "dataset_name": "mls-tasks",
                        "nr_result": args.get('num_results')
                        }
        pprint(request_data)
        
        try:
            print(search_searcher_api.api_client.configuration.host)
            api_response = search_searcher_api.post_dense_retrieval(body=request_data)
        
            # print(api_response)
            # pprint(api_response)
            
            # for r in api_response:
            #     d = DtoDenseSearchResponse(cid=r.cid, uid=r.uid, id = r.id, similarity=r.similarity)
            #     print(d)
            
            d = DtoDenseSearchResponseList(results=api_response.results).to_dict()
            response = jsonify(d)
            
            return response, HTTPStatus.OK
        except ApiException as e:
       
            return ("Exception when calling Api-> %s\n" % e)
        
        # return request_data
    

## --------------- Unit Search ----------------- ##
parser_unit_search = reqparse.RequestParser()
parser_unit_search.add_argument('requirements', action='split', type=str, location='args')
parser_unit_search.add_argument('target', action='split', type=str, location='args')

from .dto import dto_unit_search_response
ns_search_srv.models[dto_unit_search_response.name] = dto_unit_search_response

@ns_search_srv.route('/unit-search', endpoint="unit_search")
class UnitSearch(Resource):
    @ns_search_srv.expect(parser_unit_search)
    @ns_search_srv.marshal_with(dto_unit_search_response)
    def get(self):
        request_data = dict(parser_unit_search.parse_args())
        pprint(request_data)
        
        
        
        
        response = {"unit_ids": []}
        return response, HTTPStatus.OK

# @ns_search_srv.route('/search_service/add-new-nugget', endpoint="add_new_nugget")
# class

from .dto import dto_search_events_request
ns_search_srv.models[dto_search_events_request.name] = dto_search_events_request

@ns_search_srv.route('/search/events', endpoint='search_events')
class SearchEvents(Resource):
    @ns_search_srv.expect(dto_search_events_request)
    def post(self):
        request_data = ns_search_srv.payload
        pprint(request_data)
        print(type(request_data))
        
        try:
            if request_data["method"].lower() == "put":
                print("method is put")
                # add the task to the dataset
                
            elif request_data["method"].lower() == "delete":
                print("method is delete")
                # delete the task from the dataset
                
                
            else:
                raise ValueError("Invalid method! Please give either PUT or DELETE.")
            
            return {"msg": "201"}, HTTPStatus.CREATED
        except ValueError as e:
            return {"msg": e.args[0]}, HTTPStatus.BAD_REQUEST