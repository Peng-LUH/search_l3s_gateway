## import libraries
from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
import requests, json
import os, socket
from dotenv import load_dotenv
load_dotenv()



from l3s_aimeta_client.rest import ApiException
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
aims_course_title_api = l3s_aimeta_client.CourseTitleApi(api_client=client_l3s_aimeta)
aims_course_content_tags_api  = l3s_aimeta_client.ContentTagsApi(api_client=client_l3s_aimeta)
aims_course_context_tags_api  =l3s_aimeta_client.ContextTagsApi(api_client=client_l3s_aimeta)
aims_course_taught_skils_api = l3s_aimeta_client.ExistingAndNewSkillsApi(api_client=client_l3s_aimeta)
aims_course_learning_goals_api = l3s_aimeta_client.LearningGoalApi(api_client=client_l3s_aimeta)
aims_course_quiz_api = l3s_aimeta_client.QuizApi(api_client=client_l3s_aimeta)

# recsys_random_api = l3s_search_client.RandomApi(api_client=client_l3s_search)
# search_metadata_api = l3s_aimeta_client.MetadataApi(api_client=client_l3s_aimeta)

from swagger_client.l3s_aimeta_client.models.dto_summary_response import DtoSummaryResponse
from swagger_client.l3s_aimeta_client.models.dto_quiz_questions_response import DtoQuizQuestionsResponse
from swagger_client.l3s_aimeta_client.models.dto_quiz_item import DtoQuizItem
from swagger_client.l3s_aimeta_client.models.dto_quiz_questions_response_item import DtoQuizQuestionsResponseItem
from swagger_client.l3s_aimeta_client.models.all_of_dto_quiz_questions_response_results import AllOfDtoQuizQuestionsResponseResults
from swagger_client.l3s_aimeta_client.models.all_of_dto_quiz_questions_response_item_quiz_questions import AllOfDtoQuizQuestionsResponseItemQuizQuestions
## -------------------- create namespace -------------------- ##
ns_aimeta_srv = Namespace("AI-Meta Service", validate=True, description="downstream endpoints for aimeta services")

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
        

## -------------------- Course summary -------------------- ##

from .dto import dto_completion_task_summary_response_item, dto_completion_task_summary_response
ns_aimeta_srv.models[dto_completion_task_summary_response_item.name] = dto_completion_task_summary_response_item
ns_aimeta_srv.models[dto_completion_task_summary_response.name] = dto_completion_task_summary_response


@ns_aimeta_srv.route("/completions/<string:task_id>/summary", endpoint="aims_summary")
class AiMetaCourseSummary(Resource):
    @ns_aimeta_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_aimeta_srv.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_aimeta_srv.marshal_with(dto_completion_task_summary_response)
    def get(self, task_id):
        "Get summary of the Task"

        results = {
                "task_id": task_id,
                "summary": ' '
                }  
        try:      
            api_response = aims_course_summary_api.get_get_summary(task_id=task_id)
            return {"message": "success", "results":api_response.results}, HTTPStatus.OK
        
        except ValueError as e:
            return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except FileExistsError as e:
            return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
        
        except AssertionError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except ApiException as e:
                api_exception_body = e.body
                decoded_body = api_exception_body.decode('utf-8')
                try:
                    json_content = json.loads(decoded_body)
                    return {"message": json_content.get("message"), "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                except json.JSONDecodeError as json_e:
                    return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                
        except Exception as e:
            return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR



## ----------------- titles --------------- ##


from .dto import dto_completion_title_response_item, dto_completion_title_response
ns_aimeta_srv.models[dto_completion_title_response_item.name] = dto_completion_title_response_item
ns_aimeta_srv.models[dto_completion_title_response.name] = dto_completion_title_response

@ns_aimeta_srv.route('/completions/<string:task_id>/title')
class CompletionTaskTitle(Resource):
    @ns_aimeta_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_aimeta_srv.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_aimeta_srv.marshal_with(dto_completion_title_response)
    def get(self, task_id):
        "Generate titles of the Task"

        results = {
                "task_id": task_id,
                "title": [ ]
                }  
        try:      
            api_response = aims_course_title_api.get_get_title(task_id=task_id)
            return {"message": "success", "results":api_response.results}, HTTPStatus.OK
        
        except ValueError as e:
            return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except FileExistsError as e:
            return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
        
        except AssertionError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except ApiException as e:
                api_exception_body = e.body
                decoded_body = api_exception_body.decode('utf-8')
                try:
                    json_content = json.loads(decoded_body)
                    return {"message": json_content.get("message"), "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                except json.JSONDecodeError as json_e:
                    return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                
        except Exception as e:
            return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR


## ----------------- Content Tags --------------- ##

from .dto import dto_completion_content_tags_response_item, dto_completion_content_tags_response
ns_aimeta_srv.models[dto_completion_content_tags_response_item.name] = dto_completion_content_tags_response_item
ns_aimeta_srv.models[dto_completion_content_tags_response.name] = dto_completion_content_tags_response

@ns_aimeta_srv.route('/completions/<string:task_id>/content-tags')
class CompletionTaskContentTags(Resource):
    @ns_aimeta_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_aimeta_srv.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_aimeta_srv.marshal_with(dto_completion_content_tags_response)
    def get(self, task_id):
        "Generate Content tags of the Task"
        results = {
                 "task_id": task_id,
                 "content_tags": []
                    }
        try:      
            api_response = aims_course_content_tags_api.get_get_content_keywords(task_id=task_id)
            return {"message": "success", "results":api_response.results}, HTTPStatus.OK
        
        except ValueError as e:
            return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except FileExistsError as e:
            return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
        
        except AssertionError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except ApiException as e:
                api_exception_body = e.body
                decoded_body = api_exception_body.decode('utf-8')
                try:
                    json_content = json.loads(decoded_body)
                    return {"message": json_content.get("message"), "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                except json.JSONDecodeError as json_e:
                    return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                
        except Exception as e:
            return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR



## ----------------- Context Tags --------------- ##

from .dto import dto_completion_context_tags_response_item, dto_completion_context_tags_response
ns_aimeta_srv.models[dto_completion_context_tags_response_item.name] = dto_completion_context_tags_response_item
ns_aimeta_srv.models[dto_completion_context_tags_response.name] = dto_completion_context_tags_response

@ns_aimeta_srv.route('/completions/<string:task_id>/context-tags')
class CompletionTaskContextTags(Resource):
    @ns_aimeta_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_aimeta_srv.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_aimeta_srv.marshal_with(dto_completion_context_tags_response)
    def get(self, task_id):
        "Generate Context tags of the Task"
        results = {
                 "task_id": task_id,
                 "context_tags": []
                    }
        try:      
            api_response = aims_course_context_tags_api.get_get_context_keywords(task_id=task_id)
            return {"message": "success", "results":api_response.results}, HTTPStatus.OK
        
        except ValueError as e:
            return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except FileExistsError as e:
            return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
        
        except AssertionError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except ApiException as e:
                api_exception_body = e.body
                decoded_body = api_exception_body.decode('utf-8')
                try:
                    json_content = json.loads(decoded_body)
                    return {"message": json_content.get("message"), "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                except json.JSONDecodeError as json_e:
                    return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                
        except Exception as e:
            return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR



## ----------------- quiz questions --------------- ##
from .dto import completion_quiz_item, dto_completion_quiz_questions_response_item, dto_completion_quiz_questions_response
ns_aimeta_srv.models[completion_quiz_item.name] = completion_quiz_item
ns_aimeta_srv.models[dto_completion_quiz_questions_response_item.name] = dto_completion_quiz_questions_response_item
ns_aimeta_srv.models[dto_completion_quiz_questions_response.name] = dto_completion_quiz_questions_response

@ns_aimeta_srv.route('/completions/<string:task_id>/quiz-questions')
class CompletionTaskQuizQuestions(Resource):
    @ns_aimeta_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_aimeta_srv.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_aimeta_srv.marshal_with(dto_completion_quiz_questions_response)
    def get(self, task_id):
        "Generate a quiz of the Task"
        results = {
            "task_id": task_id,
            "quiz_questions": {
                "wissen": [ ],
                "verstehen": [ ],
                "anwenden": [ ]
                                }
            }

        try:      
            api_response = aims_course_quiz_api.get_get_quiz(task_id=task_id)

            response_data = DtoQuizQuestionsResponse(message=api_response.message, results=api_response.results).to_dict()

            return {"message": response_data["message"], "results": response_data["results"]}, HTTPStatus.OK
        
        except ValueError as e:
            return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except FileExistsError as e:
            return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
        
        except AssertionError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except ApiException as e:
                api_exception_body = e.body
                decoded_body = api_exception_body.decode('utf-8')
                try:
                    json_content = json.loads(decoded_body)
                    return {"message": json_content.get("message"), "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                except json.JSONDecodeError as json_e:
                    return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                
        except Exception as e:
            return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
    
    
## ------------- taught skills ---------------- ##
from .dto import dto_completion_new_existing_skills_response_item, dto_completion_new_existing_skills_response
ns_aimeta_srv.models[dto_completion_new_existing_skills_response_item.name] = dto_completion_new_existing_skills_response_item
ns_aimeta_srv.models[dto_completion_new_existing_skills_response.name] = dto_completion_new_existing_skills_response

@ns_aimeta_srv.route('/completions/<string:task_id>/taught-skills')
class CompletionTaskTaughtSkills(Resource):
    @ns_aimeta_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_aimeta_srv.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_aimeta_srv.marshal_with(dto_completion_new_existing_skills_response)
    def get(self, task_id):
        "Generate new skills and retrieve existing skills from the given learning unit."

        results = {
                "task_id": task_id,
                "new_skills": [ ],
                "existing_skills": [ ] 
                }
        

        try:      
            api_response = aims_course_taught_skils_api.get_get_taught_skills(task_id=task_id)
            return {"message": "success", "results":api_response.results}, HTTPStatus.OK
        
        except ValueError as e:
            return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except FileExistsError as e:
            return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
        
        except AssertionError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except ApiException as e:
                api_exception_body = e.body
                decoded_body = api_exception_body.decode('utf-8')
                try:
                    json_content = json.loads(decoded_body)
                    return {"message": json_content.get("message"), "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                except json.JSONDecodeError as json_e:
                    return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                
        except Exception as e:
            return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR

## ------------- Learning Goals ---------------- ##

from .dto import dto_completion_learning_goal_response_item, dto_completion_learning_goal_response
ns_aimeta_srv.models[dto_completion_learning_goal_response_item.name] = dto_completion_learning_goal_response_item
ns_aimeta_srv.models[dto_completion_learning_goal_response.name] = dto_completion_learning_goal_response

@ns_aimeta_srv.route('/completions/<string:task_id>/learning-goals')
class CompletionTaskLearningGoals(Resource):
    @ns_aimeta_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_aimeta_srv.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_aimeta_srv.marshal_with(dto_completion_learning_goal_response)
    def get(self, task_id):
        "Generate Learnng Goals of the Task"
        results = {
                "task_id": task_id,
                "learning_goals": [ ]
                }  
        try:      
            api_response = aims_course_learning_goals_api.get_get_learning_goal(task_id=task_id)
            return {"message": "success", "results":api_response.results}, HTTPStatus.OK
        
        except ValueError as e:
            return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except FileExistsError as e:
            return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
        
        except AssertionError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
        
        except ApiException as e:
                api_exception_body = e.body
                decoded_body = api_exception_body.decode('utf-8')
                try:
                    json_content = json.loads(decoded_body)
                    return {"message": json_content.get("message"), "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                except json.JSONDecodeError as json_e:
                    return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
                
        except Exception as e:
            return {"message": e, "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR

