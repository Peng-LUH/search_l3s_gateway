import os, socket, requests, json, dataclasses
from pprint import pprint
from http import HTTPStatus


from flask import request, jsonify, redirect, url_for, current_app
from flask_restx import Namespace, Resource, fields
from flask_restx.inputs import boolean
from werkzeug.exceptions import BadRequest
from requests.exceptions import InvalidURL

from l3s_gateway_api.util import util
from l3s_gateway_api import db
from l3s_gateway_api.models.document import Document

## ------------ config: l3s_search_client --------------- ##
from swagger_client import l3s_search_client
l3s_search_config = l3s_search_client.Configuration()
# l3s_search_config.host = "http://127.0.0.1:9043/l3s-search/"
l3s_search_config.host = os.getenv('L3S_SEARCH_HOST')
print("*"*80)
print("l3s-search-service-host: ", l3s_search_config.host)
print("*"*80)
client_l3s_search = l3s_search_client.ApiClient(configuration=l3s_search_config)
search_searcher_api = l3s_search_client.SearcherApi(api_client=client_l3s_search)
search_metadata_api = l3s_search_client.MetadataApi(api_client=client_l3s_search)

## ----------------- import dtos from l3s_search_client ----------------- ##
from swagger_client.l3s_search_client.rest import ApiException
from swagger_client.l3s_search_client.models.dto_dense_search_response_list import DtoDenseSearchResponseList
from swagger_client.l3s_search_client.models.dto_dataset_list import DtoDatasetList
from swagger_client.l3s_search_client.models.dto_encode_type_list import DtoEncodeTypeList

## ------------------- config: sse_search_client ----------------- ##
from swagger_client import sse_search_client
sse_search_config = sse_search_client.Configuration()
sse_search_config.host = os.getenv('SSE_SEARCH_HOST')
print("*"*80)
print("sse-search-service-host: ", sse_search_config.host)
print("*"*80)

client_sse_search = sse_search_client.ApiClient(configuration=sse_search_config)
sse_skill_api = sse_search_client.SkillApi(api_client=client_sse_search)
sse_learningunit_api = sse_search_client.LearningUnitsApi(api_client=client_sse_search)
sse_learningpath_api = sse_search_client.LearningPathApi(api_client=client_sse_search)
sse_user_api = sse_search_client.UserApi(api_client=client_sse_search)

## ----------------- import dtos from sse_search_client ----------------- ##
# from swagger_client.l3s_search_client.models.dto_encode_type_list import DtoEncodeTypeList
from swagger_client.sse_search_client.models.skill_list_dto import SkillListDto
from swagger_client.sse_search_client.models.search_learning_unit_list_dto import SearchLearningUnitListDto

## ----------------------- Namespace ------------------------ ##
ns_search_srv = Namespace("Search Service", 
                          validate=True, 
                          description="downstream endpoints for search services"
                          )


# SEARCH_BASE_URL = f'http://{os.getenv("HOST_IP")}:{os.getenv("L3S_SEARCH_PORT")}'
# with current_app.request_context():
#     print(request.host_url)

@ns_search_srv.route('/test', endpoint='test', doc=False)
class Test(Resource):
    def get(self):
        host_url = request.host_url
        return {"message": "success","results": host_url}, HTTPStatus.OK


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
        url = l3s_search_config.host
        print(url)
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
            result.update({"status": e.args[0]})
            return result, HTTPStatus.NOT_FOUND
        except InvalidURL as e:
            result = {"host_url": url}
            result.update({"status": e.args[0]})
            return result, HTTPStatus.BAD_REQUEST
        
        # return {"URL": requests.head(url).status_code}, HTTPStatus.OK




## ----------------------------- Updater ------------------------------ ##
# from .schema import DocumentSchema
# schema_document = DocumentSchema()
# schema_documents = DocumentSchema(many=True)

# @ns_search_srv.route('/updater', endpoint="l3s_gateway_search_service_updater")
# class SearcherUpdator(Resource):
#     def get(self):
#         '''update l3s-search-service'''
#         ## 1. check whether the database is clean
#         if len(db.session.dirty) > 0 or len(db.session.new) > 0:
#             print("*** Exist not commited work. Committing to the database ***")
#             db.session.commit()
#             print("*** Database commit done ***")

#         ## 2. fetch data for skills & paths
        

#         db_docs = Document.query.all()
#         documents = schema_documents.dump(db_docs)
#         request_data = {"documents": documents}
        
#         # response = requests.post('http://localhost:9043/l3s-search/searcher/searcher-update', json=request_data)
#         response = search_searcher_api.post_searcher_update(body=request_data)
#         print(response.json())
            
#         return response.json(), HTTPStatus.OK
    
#         # if not flag_db_is_modified:
#         #     return {"message": "no change in database found"}, HTTPStatus.OK
#         # else:
#         #     ## if db is modified, send new data to serch service
#         #     documents = Document.query.all()
#         #     document_list = schema_documents.dump(documents)
#         #     return document_list


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
        """get the name of datasets"""
        
        try:
            api_response = search_metadata_api.get_get_datasets()
            response_data = DtoDatasetList(results=api_response.results).to_dict()
            if response_data == []:
                response = {"message": "No datasets found", "results": []}
                return response, HTTPStatus.OK
            datasets = []
            for r in response_data["results"]:
                datasets.append(r["name"])   
            
            response = {"message": "success", "results": datasets}
            return response, HTTPStatus.OK
        except ValueError as e:
            response = {"message": e.args[0], "results": []}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR
        except FileNotFoundError as e:
            response = {"message": e.args[0], "results": []}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR
        except FileExistsError as e:
            response = {"message": e.args[0], "results": []}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR


@ns_search_srv.route('/encode-type', endpoint="get_encode_type")
class SearchServiceEncodeTypes(Resource):
    @ns_search_srv.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_search_srv.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_search_srv.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_search_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def get(self):
        """get the name of encoding types as list"""
        try:
            api_response = search_metadata_api.get_get_encoding_type()
            response_data = DtoEncodeTypeList(results=api_response.results).to_dict()
            encode_types = response_data.get("results")
            response = {"message":"success", "results": encode_types}
            return response, HTTPStatus.OK
        except ValueError as e:
            response = {"message": e.args[0], "results": []}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR
        except FileNotFoundError as e:
            response = {"message": e.args[0], "results": []}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR
        except FileExistsError as e:
            response = {"message": e.args[0], "results": []}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR
    
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


from werkzeug.exceptions import InternalServerError
from flask_restx import reqparse
parser_search_user = reqparse.RequestParser()
# parser_search_user.add_argument('user_id', type=str, location='path', default='1')
parser_search_user.add_argument('owner', type=str, action='append', location='args', default='None')
parser_search_user.add_argument('query', type=str, required=True, location='args', default='Wirkleistung von Wechselspannungen')
parser_search_user.add_argument('use_skill_profile', type=boolean, location='args', default=False)
parser_search_user.add_argument('use_learning_profile', type=boolean, location='args', default=False)
parser_search_user.add_argument('entity_type', type=str, location='args', default='all')
parser_search_user.add_argument('num_results', type=int, location='args', default=0)

from .dto import dto_search_response, dto_search_response_list
ns_search_srv.models[dto_search_response.name] = dto_search_response
ns_search_srv.models[dto_search_response_list.name] = dto_search_response_list

### Connection: search services
@ns_search_srv.route('/search/<string:user_id>', endpoint="search_user_id")
class SearchService(Resource):
    @ns_search_srv.expect(parser_search_user)
    @ns_search_srv.marshal_with(dto_search_response_list)
    def get(self, user_id):
        args=parser_search_user.parse_args()
                        
        if args.get('owner') == []:
            owner = ""
        else:
            owner = args.get('owner')
            
        request_data = {
                        "user_id": user_id,
                        "owner": owner,
                        "query": args.get('query'),
                        "use_skill_profile": args.get("use_skill_profile"),
                        "use_learning_profile": args.get("use_learning_profile"),
                        "language_model": "bert-base-german-cased",
                        "index_method": "flat-l2",
                        "entity_type": args.get("entity_type"),
                        "nr_result": args.get('num_results')
                        }
        
        try:
            api_response = search_searcher_api.post_dense_retrieval(body=request_data)
            response = DtoDenseSearchResponseList(message=api_response.message,
                                                  results=api_response.results).to_dict()
            print(response)
            return response, HTTPStatus.OK
        except ApiException as e:
            response = {"message": ("Exception when calling Api-> %s\n" % e), "results": []}
            return response, HTTPStatus.BAD_REQUEST
        except InternalServerError as e:
            response = {"message": ("Exception when calling Api-> %s\n" % e), "results": []}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR
    

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

 
 
 
## ------------------- sse --------------------------------------- ##

# @ns_search_srv.route('/sync/skills', endpoint='search_init_skills')
# class IinitSkills(Resource):
#     # @ns_search_srv.expect(dto_update_skill_request)
#     def get(self):
#         '''sync the data for skills '''
#         ## -------- Step 1: Get skills from SSE ----------
#         # response = requests.get('https://staging.sse.uni-hildesheim.de:9011/skill-repositories/skill')
#         # print(len(response.json().get('skills')))
#         # request_data = response.json()
        
#         try: 
#             response = sse_skill_api.skill_mgmt_controller_get_all_skills()
#             d = SkillListDto(skills=response.skills)
#             request_data = d.to_dict()
#             # print(request_data.get("skills")[0])
  
#             if request_data["skills"] == []:
#                 raise ValueError("No skills retrieved!")
            
#             return request_data.get("skills")[0], HTTPStatus.OK
#         except ValueError as e:
#             return {"message": e.args[0]}, HTTPStatus.BAD_REQUEST
            
#         # print(type(request_data.get("skills")[0].get("level")))
#         # pprint(request_data.get("skills")[0])
        
#         ## -------- Step 2: send data to database service ----------- ##
#         # request_url = util.get_request_url(endpoint='api.db_init_skills')
#         # r = requests.post(request_url, json=request_data)
#         # print(r.json())
        
#         # return r.json(), r.status_code
    


    