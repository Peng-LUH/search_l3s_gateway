## import libraries
from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
import requests, json
import os, socket


# config: l3s_aimeta_cleint
from swagger_client import l3s_aimeta_client
l3s_aimeta_config = l3s_aimeta_client.Configuration()
# l3s_aimeta_config.host = "http://localhost:9043/l3s-search"
l3s_aimeta_config.host = os.getenv('L3S_AIMETA_HOST')
print("*"*80)
print("l3s-aimeta-service-host: ", l3s_aimeta_config.host)
print("*"*80)
client_l3s_aimeta = l3s_aimeta_client.ApiClient(configuration=l3s_aimeta_config)
# l3s recsys api registration
aims_course_summary_api = l3s_aimeta_client.CourseSummaryApi(api_client=client_l3s_aimeta)
# recsys_random_api = l3s_search_client.RandomApi(api_client=client_l3s_search)
# search_metadata_api = l3s_aimeta_client.MetadataApi(api_client=client_l3s_aimeta)


## -------------------- create namespace -------------------- ##
ns_aimeta_srv = Namespace("AI-Meta Service", validate=True, description="downstream endpoints for aimeta services")


@ns_aimeta_srv.route('/aimeta-service/course-summary/<string:id>', endpoint="aims_course_summary")
class AiMetaCourseSummary(Resource):
    def get(self, id):
        api_response = aims_course_summary_api.get_get_summary(id=id)
        print(api_response)
        return {"msg": "ok"}, HTTPStatus.OK

## ------------------- check connection -------------------- ##
from .dto import dto_aimeta_connection_response
ns_aimeta_srv.models[dto_aimeta_connection_response.name] = dto_aimeta_connection_response

@ns_aimeta_srv.route('/connection', endpoint="aimeta_service_connection")
class AiMetaOk(Resource):
    @ns_aimeta_srv.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_aimeta_srv.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_aimeta_srv.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_aimeta_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    @ns_aimeta_srv.marshal_with(dto_aimeta_connection_response)
    def get(self):
        url = l3s_aimeta_config.host
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
            result.update({"connection": e.strerror})
            return result, HTTPStatus.NOT_FOUND



## ------------------ completion task ----------------- ##
from .dto import dto_completion_task_response
ns_aimeta_srv.models[dto_completion_task_response.name] = dto_completion_task_response

@ns_aimeta_srv.route('/completions/<string:task_id>', endpoint="completion_task")
class CompletionTask(Resource):
    @ns_aimeta_srv.marshal_with(dto_completion_task_response)
    def get(self, task_id):
        """in progress"""
        print(task_id)
        return



## ------------------ completion unit ---------------- ##
# from .dto import dto_completion_unit_response
# ns_aimeta_srv.models[dto_completion_unit_response.name] = dto_completion_unit_response

# @ns_aimeta_srv.route('/completions/<string:task_id>/unit', endpoint="completion_unit")
# class CompletionTaskTitle(Resource):
#     @ns_aimeta_srv.param("request_type", description="type of request")
#     @ns_aimeta_srv.marshal_with(dto_completion_unit_response)
#     def get(self, task_id):
#         print(task_id)
#         return

from .dto import dto_completion_task_title_response
ns_aimeta_srv.models[dto_completion_task_title_response.name] = dto_completion_task_title_response

@ns_aimeta_srv.route('/completions/<string:task_id>/title')
class CompletionTaskTitle(Resource):
    @ns_aimeta_srv.marshal_with(dto_completion_task_title_response)
    def get(self, task_id):
        """in progress"""
        print(task_id)
        return
    


from .dto import dto_completion_task_summary_response
ns_aimeta_srv.models[dto_completion_task_summary_response.name] = dto_completion_task_summary_response

@ns_aimeta_srv.route('/completions/<string:task_id>/summary')
class CompletionTaskSummary(Resource):
    @ns_aimeta_srv.marshal_with(dto_completion_task_summary_response)
    def get(self, task_id):
        """in progress"""
        print(task_id)
        return
    


from .dto import dto_completion_task_content_tags_response
ns_aimeta_srv.models[dto_completion_task_content_tags_response.name] = dto_completion_task_content_tags_response

@ns_aimeta_srv.route('/completions/<string:task_id>/content-tags')
class CompletionTaskContentTags(Resource):
    @ns_aimeta_srv.marshal_with(dto_completion_task_content_tags_response)
    def get(self, task_id):
        """in progress"""
        print(task_id)
        return


from .dto import dto_completion_task_context_tags_response
ns_aimeta_srv.models[dto_completion_task_context_tags_response.name] = dto_completion_task_context_tags_response

@ns_aimeta_srv.route('/completions/<string:task_id>/context-tags')
class CompletionTaskContextTags(Resource):
    @ns_aimeta_srv.marshal_with(dto_completion_task_content_tags_response)
    def get(self, task_id):
        """in progress"""
        print(task_id)
        return
    
## ----------------- quiz questions --------------- ##
from .dto import dto_completion_task_quiz_questions_response
ns_aimeta_srv.models[dto_completion_task_quiz_questions_response.name] = dto_completion_task_quiz_questions_response

@ns_aimeta_srv.route('/completions/<string:task_id>/quiz-questions')
class CompletionTaskQuizQuestions(Resource):
    @ns_aimeta_srv.marshal_with(dto_completion_task_quiz_questions_response)
    def get(self, task_id):
        """in progress"""
        print(task_id)
        return
    
    
## ------------- taught skills ---------------- ##
from .dto import dto_completion_task_taught_skills_response
ns_aimeta_srv.models[dto_completion_task_taught_skills_response.name] = dto_completion_task_taught_skills_response

@ns_aimeta_srv.route('/completions/<string:task_id>/taught-skills')
class CompletionTaskTaughtSkills(Resource):
    @ns_aimeta_srv.marshal_with(dto_completion_task_taught_skills_response)
    def get(self, task_id):
        """in progress"""
        print(task_id)
        return