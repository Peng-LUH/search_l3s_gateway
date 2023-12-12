from http import HTTPStatus
import os, json
import requests
# import flask
from flask import request, url_for, make_response, jsonify, redirect
from pprint import pprint
import traceback, logging
# import flask-restx
from flask_restx import Namespace, Resource, fields
from flask_restx import reqparse
# Exceptions
from werkzeug.routing.exceptions import BuildError
# utils
from l3s_gateway_api.util.util import get_request_url
# import database and models
from l3s_gateway_api import db
# from l3s_gateway_api.models.test import Test
# from l3s_gateway_api.models.task import Task
from l3s_gateway_api.models.document import Document

ns_database = Namespace("L3S Database", validate=True, description="endpoints to communicate with the mls")

SHOW_PRIVATE_ENDPOINT = True
print(SHOW_PRIVATE_ENDPOINT)

## import flask-restx-model
from l3s_gateway_api.api.database.dto import (
    test_model,
    service_model,
    request_model,
    retrieve_model,
)
ns_database.models[test_model.name] = test_model
ns_database.models[service_model.name] = service_model
ns_database.models[request_model.name] = request_model
ns_database.models[retrieve_model.name] = retrieve_model

## Schemas
from .schema import DocumentSchema
schema_document = DocumentSchema()
schema_documents = DocumentSchema(many=True)

## ------------ config: l3s_search_client --------------- ##
from swagger_client import l3s_search_client
l3s_search_config = l3s_search_client.Configuration()
# l3s_search_config.host = "http://127.0.0.1:9043/l3s-search/"
l3s_search_config.host = os.getenv('L3S_SEARCH_HOST')
print("*"*80)
print("l3s-search-service-host: ", l3s_search_config.host)
print("*"*80)

client_l3s_search = l3s_search_client.ApiClient(configuration=l3s_search_config)
# l3s recsys api registration
search_searcher_api = l3s_search_client.SearcherApi(api_client=client_l3s_search)
search_metadata_api = l3s_search_client.MetadataApi(api_client=client_l3s_search)

from swagger_client.l3s_search_client.models.dto_searcher_update_response import DtoSearcherUpdateResponse


## -------------------------------- Check Secret ------------------------ ##
parser_secret = reqparse.RequestParser()
parser_secret.add_argument('secret_key', type=str, location='args')
@ns_database.route('/check_secret')
class CheckSecretKey(Resource):
    @ns_database.expect(parser_secret)
    def get(self):
        request_data = parser_secret.parse_args()
        if request_data["secret_key"] == os.getenv('MLS_CLIENT_SECRET'):
            return {"message": "valid secret key"}, HTTPStatus.OK
        else:
            return {"message": "invalid secret key"}, HTTPStatus.BAD_REQUEST

## -------------------------------- Sync -------------------------------- ##
from .logic import (get_list_of_skills, 
                    list_of_skills_transformer,
                    get_list_of_learning_units,
                    transformer_list_of_learning_units,
                    db_skill_updater,
                    db_task_updater,
                    get_task_content
                    )

from .dto import dto_skill_list, dto_skill, dto_sync, dto_sync_list
ns_database.models[dto_skill.name] = dto_skill
ns_database.models[dto_skill_list.name] = dto_skill_list
ns_database.models[dto_sync.name] = dto_sync
ns_database.models[dto_sync_list.name] = dto_sync_list

@ns_database.route('/sync', endpoint='l3s_db_sync')
class L3SDatabseSync(Resource):
    # @ns_database.marshal_with(dto_sync_list)
    def get(self):
        ''' l3s database synchronization '''
        sync_results = []
        
        ## Sync: Skills
        request_url_skill = get_request_url(endpoint_url=url_for('api.l3s_db_sync_skills'))
        response_skill = requests.get(request_url_skill)
        response_skill_json = response_skill.json()
        print('print response skill json\n')
        pprint(response_skill_json)
        response_skill_json["entity_type"] = "skill"
        response_skill_json["status_code"] = response_skill.status_code
        sync_results.append(response_skill_json)
        
        
        ## ------------------- Sync: Learning Paths -------------------
        
        # request_url_path = get_request_url(endpoint_url=url_for('api.l3s_db_sync_learning_paths'))
        # response_path = requests.get(request_url_path)
        
        
        ## ------------------- Sync: Tasks/ Learning-Units ---------------------
        
        # request_url_task = get_request_url(endpoint_url=url_for('api.l3s_db_sync_tasks'))
        # response_task = requests.get(request_url_task)

        
        ## send data to l3s-search-service/searcher/sercher-update
        ## get data
        docs = Document.query.all()
        request_data = {"secret": os.getenv('MLS_CLIENT_SECRET'), 
                        "documents": schema_documents.dump(docs)}
        print(request_data)
        response = search_searcher_api.post_searcher_update(body=request_data)
        d = DtoSearcherUpdateResponse(message=response.message).to_dict()
        return d
        
        
## ----------------------- Sync: Skills ---------------------------- ##
from .dto import dto_sync_results, dto_sync_response
ns_database.models[dto_sync_results.name] = dto_sync_results
ns_database.models[dto_sync_response.name] = dto_sync_response

@ns_database.route('/sync/skills', endpoint='l3s_db_sync_skills')
class L3SDBSyncSkills(Resource):
    # @ns_search_srv.expect(dto_update_skill_request)
    @ns_database.response(int(HTTPStatus.OK), description="Success: Skills are up to date")
    @ns_database.response(int(HTTPStatus.CREATED), description="Success: Skills are sychronized")
    # @ns_database.marshal_with(dto_sync_response)
    def get(self):
        ''' sync the data for skills '''
        ## -------- Step 1: Get skills from SSE ----------
        try: 
            list_of_skills = get_list_of_skills()
            
            ## check if list is empty
            if list_of_skills == []:
                raise ValueError("No skills retrieved!")
            
            # list_of_skills = list_of_skills[:2]
            # pprint(list_of_skills)
            
            ## transform the list
            list_of_skills = list_of_skills_transformer(list_of_skills)
            pprint(list_of_skills[:2])
            
            ## update
            num_adds, num_updates = db_skill_updater(list_of_skills[:2])
            
            results = {
                "num_adds": num_adds,
                "num_updates": num_updates
            }
            
            if num_adds==0 and num_updates==0:
                return {"message": "success", "results": results}, HTTPStatus.OK
            
            # return request_data.get("skills")[0], HTTPStatus.OK
            return {"message": "success", "results": results}, HTTPStatus.CREATED
        except ValueError as e:
            results = {
                "num_adds": "N.A.",
                "num_updates": "N.A."
            }
            return {"message": e.args[0], "results": {}}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"message": logging.error(traceback.format_exc()), "results": {}}, HTTPStatus.INTERNAL_SERVER_ERROR


## --------------------------- Sync: Learning Path --------------------------- ##
@ns_database.route('/sync/learning-paths', endpoint='l3s_db_sync_learning_paths')
class L3SDBSyncLearningPaths(Resource):
    def get(self):
        '''sync the data for learning paths'''
        
        return {"message": "method not implemented.", "results": []}
    

@ns_database.route('/sync/tasks', endpoint='l3s_db_sync_tasks')
class InitLearningUnits(Resource):
    @ns_database.response(int(HTTPStatus.OK), description="Success: Tasks are up-to-date")
    @ns_database.response(int(HTTPStatus.CREATED), description="Success: Tasks are sychronized")
    @ns_database.marshal_with(dto_sync_response)
    def get(self):
        '''sync the data for learning units/tasks'''
        
        return {"message": "method not implemented.", "results": []} 
        ## get the list of learning units from sse
        list_of_learning_units = get_list_of_learning_units()
        
        list_of_learning_units = transformer_list_of_learning_units(list_of_learning_units)
        pprint(list_of_learning_units[0])
        
        
        num_adds, num_updates = db_task_updater(list_of_learning_units[:2])
        results = {"num_adds": num_adds, "num_updates": num_updates}
        
        if num_adds==0 and num_updates==0:
            return {"message": "Success: Tasks are up-to-date.", "results": results}, HTTPStatus.OK
        
        return {"message": "Success: Tasks are synchronized", "results": results}, HTTPStatus.CREATED    
        ## send request data to l3s-database/init-learning-units
        # request_url = util.get_request_url(endpoint='api.db_init_learning_units')
        # print(request_url)
        # response = requests.post(request_url, json=request_data)
        # print(response.status_code)
        
        
## ------------------------------------- Documents ----------------------------------- ##
from .dto import dto_document_delete_response, dto_document_post_request
ns_database.models[dto_document_delete_response.name] = dto_document_delete_response
ns_database.models[dto_document_post_request.name] = dto_document_post_request

@ns_database.route('/document/<string:entity_type>/<string:entity_id>', endpoint="db_doc_by_id")
class DocumentById(Resource):
    def get(self, entity_type, entity_id):
        doc = Document.query.filter_by(entity_type=entity_type, entity_id=entity_id).first()
        temp = schema_document.dump(doc)
        print(type(temp["owner"]))
        return temp
    def put(self, entity_type, entity_id):
        doc = Document.query.filter_by(entity_type=entity_type, entity_id=entity_id).first()
        doc.owner = ['1', '2', '3']
        temp = schema_document.dump(doc)
        print(type(temp["owner"]))
        return temp
    @ns_database.expect(dto_document_post_request)
    def post(self, entity_type, entity_id):
        request_data = request.json
        if entity_type not in ["task", "skill", "path"]:
            return {"message": "invalid entity type"}, HTTPStatus.BAD_REQUEST
        
        entity_id_full = f"{entity_type}/{entity_id}"
        
        doc = Document(
                       owner=[],
                       entity_id = entity_id,
                       entity_type = entity_type,
                       entity_id_full = entity_id_full,
                       contents = request_data["contents"],
                       created_at = request_data["created_at"],
                       updated_at = request_data["updated_at"]
                       )
        db.session.add(doc)
        db.session.commit()
        
        print(doc)
        return {"message": "success"}
    
    @ns_database.marshal_with(dto_document_delete_response)
    def delete(self, entity_type, id):
        try:
            it = Document.query.filter_by(entity_type=entity_type, entity_id=id).first()
            if it:
                db.session.delete(it)
                db.session.commit()
                return {"status": "success", "message": "document deleted"}
            else:
                raise FileNotFoundError(f'the requesting file with entity type: "{entity_type}" and id: "{id}" does not found.')
        except FileNotFoundError as e:
            return {"status": "failed", "message": e.args[0]}
        
         
from sqlalchemy import cast, Integer
@ns_database.route('/document/all', endpoint="db_all_document")
class DocumentAll(Resource):
    def get(self):
        docs = Document.query.order_by(cast(Document.entity_id, Integer)).all()
        return schema_documents.dump(docs)
    
    @ns_database.doc(delete=False)
    def delete(self):
        db.session.query(Document).delete()
        db.session.commit()
        docs = Document.query.all()
        return schema_documents.dump(docs)




## -------------------------- Search Events ---------------------------- ##
# from .dto import dto_l3s_events_request
# ns_database.models[dto_l3s_events_request.name] = dto_l3s_events_request
# @ns_database.route('/events', endpoint='l3s_events')
# class L3SEvents(Resource):
#     @ns_database.expect(dto_l3s_events_request)
#     def post(self):
#         request_data = request.json
#         pprint(request_data)
#         print(type(request_data))
#         method = request_data.get("method")
#         task_id = request_data.get("task_id")
#         entity_type = request_data.get()
        
#         try:
#             if method.lower() == "post":
                
#                 handler_task_post(task_id)
#             elif method.lower() == "put":
#                 print("Update: task {task}")
#                 handler_task_put(task_id)
#                 pass
#             elif method.lower() == "delete":
#                 print("method is delete")
                
#             else:
#                 raise ValueError("Invalid method! Please give either PUT or DELETE.")
            
#             return {"msg": "201"}, HTTPStatus.CREATED
#         except ValueError as e:
#             return {"msg": e.args[0]}, HTTPStatus.BAD_REQUEST




## ------------- Skills & LearningUnits & Paths ------------- ##
# sse calls this endpoint to inform that there are changes in the skills
# get the new data
# send it to search service
# update the data.json file in search service
# rerun encoding and indexing step
# update the version in search service
# inform gateway the changes


# from .dto import dto_learning_unit, dto_init_learning_units_request
# ns_database.models[dto_init_learning_units_request.name] = dto_init_learning_units_request
# ns_database.models[dto_learning_unit.name] = dto_learning_unit
# # from .logic import db_learning_unit_processor

# @ns_database.route('/learning-units/update', endpoint='db_learning_units_update')
# class DBLearningUnitsUpdate(Resource):
#     @ns_database.expect(dto_init_learning_units_request)
#     def post(self):
#         '''in progress'''
#         request_data = request.json
#         # lst_learning_units = request_data.get("learning_units")
#         # print(lst_learning_units[0])
#         # return {"number of learning units": len(lst_learning_units)}
#         try:
#             list_learning_units = request_data.get("learning_units")
#             ## check if list is none
#             if not list_learning_units:
#                 raise ValueError("Attribute Not Found: learningUnits")
            
#             # check the length of the list
#             if len(list_learning_units) == 0:
#                 return {"message": "no learning units received"}, HTTPStatus.OK
#             elif len(list_learning_units) > 0:
#                 pprint(list_learning_units[0])
#                 ## add learning units to database
                
                
                
#                 return {"message": "db init learning units"}, HTTPStatus.CREATED
#             else:
#                 raise ValueError("Negative list: learningUnits")
            
#             # write the list into db as document
#             # r = db_learning_unit_processor(list_learning_units)
            
#         except ValueError as e:
#             return {"message": e.args}
        
        
    

# from .dto import dto_update_paths_request
# ns_database.models[dto_update_paths_request.name] = dto_update_paths_request
# @ns_database.route('/learning-paths/update', endpoint="db_learning_paths_update")
# class DBLearningPathsUpdate(Resource):
#     @ns_database.expect(dto_update_paths_request)
#     def post(self):
#         '''in progress'''
#         request_data = request.json
#         path_id = request_data.get('path_ids')
#         method = request_data.get('method')
#         try:
#             if len(path_id) == 0:
#                 return {"message": "request contains no path id"}, HTTPStatus.OK
            
#             if method not in ['add', 'modify', 'delete']:
#                 raise ValueError('Invalid method: try add or modify or delete')
            
#             return request_data
#         except ValueError as e:
#             return {"message": e.args}, HTTPStatus.BAD_REQUEST











## ----------------  Test --------------- ##
# from .dto import dto_test_request, dto_test_response
# ns_database.models[dto_test_request.name] = dto_test_request
# ns_database.models[dto_test_response.name] = dto_test_response

# from .schema import TestSchema
# schema_test = TestSchema()
# schema_tests = TestSchema(many=True)

# # test_schema = TestsSchema()
# # tests_schema = TestsSchema(many=True)


# @ns_database.route("/data/tests", endpoint="data_tests")
# class DataTest(Resource):
#     # @ns_database.marshal_with(dto_test_response)
#     def get(self):
#         """get all the tests"""
   
        
#         test_list = Test.query.all()
#         if len(test_list) == 0:
#             return {"msg": "there is no data in the database"}
        
#         print(type(test_list))
#         print(test_list)
        
#         # test_list_dump = tests_schema.dump(test_list)
#         # print(type(test_list_dump))
#         # print(test_list_dump)
        
#         # print(tests_2_schema.dump(test_list))
        
        
#         return schema_tests.dump(test_list)
    
    
#     @ns_database.expect(dto_test_request)
#     def post(self):
#         # get the request data
#         request_data = request.json
#         print(request_data)
        
#         # write data to databank
#         new_test = Test(
#             firstList=request_data.get("firstList"), 
#             secondList=request_data.get("secondList")
#             )
        
#         db.session.add(new_test)
#         db.session.commit()
        
#         return

# @ns_database.route("/data/test/<string:id>")
# class DataTestById(Resource):
#     def get(self, id):
#         result = Test.find_by_id(id)
#         print(result)
#         result_dump = schema_tests.dump(result)
#         print(result_dump)
#         return result_dump



# @ns_database.route("/data/document/<string:>", endpoint="document_id")
# class DocumentID(Resource):
#     def get(self):
#         return
    # def post(self):
    #     return
    # def put(self):
    #     return
    # def delete(self):
    #     return

# @ns_upstream.route("/test_upstream", endpoint="test_upstream")
# class TestUpstream(Resource):
#     def get(self):
#         return {"message": "get method from test upstream endpoint."}, HTTPStatus.OK

#     @ns_upstream.expect(test_model)
#     def post(self):
#         data = request.json()
#         return data, HTTPStatus.CREATED


# @ns_upstream.route("/service-request", endpoint="service_request")
# class ServiceRequest(Resource):
#     @ns_upstream.expect(service_model)
#     @ns_upstream.response(int(HTTPStatus.CREATED), "request accepted")
#     def post(self):
#         request_data = request.json()
#         # request_data.headers['Content-Type'] = "application/json"
#         # check if company exists, if not create
#         user_id = request_data.get("user_id")
#         if user_id:
#             user = db.session.execute(db.select(User).filter_by(user_id=user_id)).first()
#             if user:
#                 user = user[0]
#             else:
#                 new_user = User(user_id = user_id)
#         # check if user exists, if not create
        
#         return request_data


# @ns_upstream.route("/retrieve-info", endpoint="retrieve_info")
# class RetrieveInfo(Resource):
#     @ns_upstream.expect(retrieve_model)
#     def post(self):
#         pass
    
    
# @ns_database.route("/get-users", endpoint="get_users")
# class GetUsers(Resource):
#     def get(self):
#         try:
#             users = User.query.all()
#             return make_response(jsonify([user.json() for user in users]), 200)
#         except:
#             return make_response(jsonify({'message': 'error getting users'}), 500)