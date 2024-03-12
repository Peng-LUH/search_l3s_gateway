import os
import json, requests

MLS_LOGIN_PAYLOAD = {
  "client_id": os.getenv("MLS_CLIENT_ID"),
  "client_secret": os.getenv("CLIENT_SECRET"),
  "username": os.getenv("MLS_USERNAME"),
  "password": os.getenv("MLS_PASSWORD"),
  "grant_type": os.getenv("MLS_GRANT_TYPE"),
}

class MLS_CONTENT_TYPE(object):
    DIRECTORIIES = "directories"
    DOCUMENTS = "documents"
    EXTERNAL_ILIAS_COURSES = "external-ilias-courses"
    FEEDBACK = "feedback"
    FORMS = "forms"
    FORM_SET = "form-sets"
    GROUPS = "groups"
    GROUP_TASK_TODOS = "group-task-todos"
    JOB = "jobs"
    ORGANIZATION = "organizations"
    PROJECT = "projects"
    PROJECT_TASK = "project-tasks"
    PROJECT_TODO = "project-todos"
    SKILL = "skills"
    TAG = "tags"
    
    TASK = "tasks"
    TASK_SKILL = "task-skills"
    TASK_FILE = "task-files"
    TASK_SET = "task-sets"
    TASK_SET_TRANSLATION = "task-set-translations"
    
    TASK_STEP = "task-steps"
    TASK_STEP_FILE = "task-step-files"
    TASK_STEP_CATEGORY = "task-step-categories"
    
    TASK_TODO = "task-todos"
    TASK_TODO_INFO = "task-todo_infos"
    TASK_TODO_FILE = "task-todo-files"
    
    USER = "users"

class MLSConnection(object):
    def get_login_response(self, login_server_url, realm, login_payload):
        """returns response as json object"""
        login_response = requests.post(login_server_url + "/realms/" + realm + "/protocol/openid-connect/token",
                data = login_payload,
                headers =  {
                "Content-Type": "application/x-www-form-urlencoded",
                }
            )
        return login_response
    
    def get_access_token(self, login_response): 
        return login_response.json()["access_token"]
    
    def get_auth_header(self, access_token, accept_header="application/ld+json"):
        auth_header =  {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
            "accept": accept_header,
            }
        return auth_header
    
    def get_response(self, base_url, content_type, auth_header):
        url = base_url+"/mls-api/"+content_type
        print(url)
        response = requests.get(url, headers=auth_header)
        
        return response