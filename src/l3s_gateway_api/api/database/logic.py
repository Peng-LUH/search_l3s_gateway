from openai import OpenAI
import os, requests
from dotenv import load_dotenv
load_dotenv()

from bs4 import BeautifulSoup
from http import HTTPStatus
from flask import jsonify
from pprint import pprint
import json
import copy

from l3s_gateway_api.util.mls_api import (
    MLS_LOGIN_PAYLOAD,
    MLSConnection
)
from l3s_gateway_api import db
from l3s_gateway_api.models.task import Task
from l3s_gateway_api.models.document import Document


MLS_BASE_URL = os.getenv("MLS_BASE_URL")
MLS_LOGIN_SERVER_URL = os.getenv("MLS_LOGIN_SERVER_URL")
MLS_REALM = os.getenv("MLS_REALM")
MLS_LOGIN_PAYLOAD={
    "client_id": os.getenv("MLS_CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET"),
    "username": os.getenv("MLS_USERNAME"),
    "password": os.getenv("MLS_USER_PASSWORD"),
    "grant_type": os.getenv("MLS_GRANT_TYPE")
}


openai_client = OpenAI()


def get_mls_access_token():
    '''Get MLS access token'''
    login_response = requests.post(MLS_LOGIN_SERVER_URL + "/realms/" + MLS_REALM + "/protocol/openid-connect/token",
        data = MLS_LOGIN_PAYLOAD,
        headers =  {
        "Content-Type": "application/x-www-form-urlencoded",
        }
    )
    mls_access_token = login_response.json()["access_token"]
    return mls_access_token


def get_mls_tasks():
    '''Get the list of tasks from MLS'''
    access_token = get_mls_access_token()
    response_tasks = requests.get(MLS_BASE_URL + "/mls-api/tasks",
                                params = {
                                    "page": "1",
                                    "pagination": "false"
                                    },
                                headers = {
                                  "Authorization": "Bearer " + access_token,
                                  "Content-Type": "application/json"
                                }
                    )
    mls_tasks = response_tasks.json().get("hydra:member")
    return mls_tasks

def get_mls_task(task_id):
    '''Get Task object from MLS by task-id'''
    
    access_token = get_mls_access_token()
    response_task = requests.get(MLS_BASE_URL + f"/mls-api/tasks/{task_id}",
                                headers = {
                                  "Authorization": "Bearer " + access_token,
                                  "Content-Type": "application/json"
                                }
                    )
    # print(response_tasks.json())
    mls_task = response_task.json()
    return mls_task

def get_mls_task_steps(task_id):
    '''Get the task steps for a task by task-id'''
    access_token = get_mls_access_token()
    response_task_steps = requests.get(MLS_BASE_URL + "/mls-api/task-steps",
                                       params={"task": f"/mls-api/tasks/{task_id}"},
                                       headers={
                                           "Authorization": "Bearer" + access_token,
                                           "Content-Type": "application/json"
                                       }
                                       )
    task_steps = response_task_steps.json().get("hydra:member")
    return task_steps


def get_content_for_task_steps(task_id):
    '''get the content for task steps for a task by task-id'''
    ## returns the list of task steps with their content for given task-id
    ## get task steps for the task
    task_steps = get_mls_task_steps(task_id=task_id)
    list_of_contents = []
    for step in task_steps:
        temp = {}
        temp["@id"] = step["@id"]
        temp["title"] = step["title"]
        html_string = step.get("content")[0]["value"]
        content = html_string_extractor(html_string)
        temp["content"] = content

        list_of_contents.append(temp)
    return list_of_contents


def get_task_content(task_id):
    '''Extract content from mls-task-obj'''
    temp = {}
    task = get_mls_task(task_id)
    temp["@id"] = task["@id"]
    temp["title"] = task["title"]
    temp["description"] = html_string_extractor(task["description"])
    
    task_steps_contents = get_content_for_task_steps(task_id)
    temp["task_steps"] = task_steps_contents
    return temp


def html_string_extractor(html_string):
    '''Extract content from html block'''
    # Use BeautifulSoup to remove HTML tags
    soup = BeautifulSoup(html_string, "html.parser")
    text_without_tags = soup.get_text()
    content = text_without_tags.replace('\n', '').replace('\xa0', '')
    return content

# def add_new_task(task_id, request_data):
#     print("*** add new task ***")
#     contents = request_data.get('contents')
    
#     new_task = Task(
#                 task_id_int = task_id,
#                 task_id_str = '/mls-api/tasks/' + str(task_id),
#                 contents = contents
#             )
    
#     db.session.add(new_task)
#     db.session.commit()
#     response = jsonify(message= f"add new task with id {task_id}")
#     response.status = HTTPStatus.OK
    
#     return response


# def update_task(task_id, request_data):
#     it = Task.query.filter_by(task_id_int=task_id).first()
#     keys = list(request_data.keys())
#     response = jsonify(message=f"update task with id {task_id}")
#     return response

# def delete_task(task_id, task):
#     print("*** delete task ***")
#     db.session.delete(task)
#     db.session.commit()
#     response = jsonify(message=f"task with task-id {task_id} is deleted")
#     response.status = HTTPStatus.OK
#     print(response)
#     return response



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
from swagger_client.sse_search_client.models.learning_path_list_dto import LearningPathListDto


def get_list_of_skills():
    response = sse_skill_api.skill_mgmt_controller_get_all_skills()
    d = SkillListDto(skills=response.skills)
    request_data = d.to_dict()
    # print(request_data.get("skills")[0])
    list_of_skills = request_data["skills"]
    return list_of_skills


def skill_transformer(skill, lst_skills):
    if not skill["nested_skills"] == []:
        ns_names = []
        for ns in skill["nested_skills"]:
            ns_item = next(item for item in lst_skills if item["id"] == ns)
            ns_names.append(ns_item["name"])
                    
            # print(ns_names)
            skill["nested_skills"] = ns_names
            
    if not skill["parent_skills"] == []:
        ps_names = []
        for ps in skill["parent_skills"]:
            ps_item = next(item for item in lst_skills if item["id"] == ps)
            ps_names.append(ps_item["name"])
        
        # print(ps_names)
        skill["parent_skills"] = ps_names
    return skill

def skill_lite(skill):
    temp = copy.copy(skill)
    temp.pop('created_at', None)
    temp.pop('updated_at', None)
    temp.pop('id', None)
    temp.pop('repository_id', None)
    return temp

def list_of_skills_transformer(list_of_skills):
    # convert the lsit of skills
    
    new_list = []
    
    for skill in list_of_skills:
        skill = skill_transformer(skill, list_of_skills)
        new_list.append(skill)
    return new_list


def dict_content_generator(my_dict):

    # Convert the dictionary to a string representation
    dict_str = ', '.join([f"{key}: {value}" for key, value in my_dict.items()])
    print(dict_str)
    # Use the OpenAI API to generate a description
    messages = [
        {"role": "system", "content": "You are a teacher with 30 years of experience. You are designed to output JSON."},
        {"role": "user", "content": f"Please give me a summary about the skill with the provided information: {dict_str}. I want this explaination of this skill to be in German. The summary must contain the following information: the name of the skill, the description of the skill, the nested skills and parent skills. The output should be in one paragraph. The key should be 'Zusammenfassung'. This summary will be used as input of word embedding for semantic search algorithm."},
    ]
    # print(prompt)
    response = openai_client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
        response_format={ "type": "json_object" },
        max_tokens=300,  # Adjust the number of tokens as needed
    )
    # print(response)
    description = response.choices[0].message.content
    print('\n\n')
    summary = json.loads(description)
    pprint(summary)
    print(type(summary))
    print('\n\n')
    print()
    content = list(summary.values())[0]
    return content
    # return
    

def db_skill_updater(lst_skills):
    ## setup counter
    num_adds = 0
    num_updats = 0
    # result = []
    ## add skills to database
    for skill in lst_skills:
        print(f"******* processing skill {skill['id']} *********")
        
        ## cast skill.level to integer
        skill["level"] = int(skill["level"])
        
        # check if the skill already exist in the db
        doc = Document.query.filter_by(entity_id=skill["id"], entity_type="skill").first()
        
        flag_doc_exists = (doc!=None)
        print(f"Already exists: {flag_doc_exists}")
        
        if flag_doc_exists:
            flag_doc_is_modified = not(doc.updated_at == skill["updated_at"])
            print(f"Is modified: {flag_doc_is_modified}")
            # check whether the skill is updated
            if not flag_doc_is_modified:
                print(f"*** skill {skill['id']} already exists and has no update")
                continue
            else: # write the info form skill to doc
                print(f"******* updating skill {skill['id']} *********")
                temp = skill_lite(skill)
                skill_content = dict_content_generator(temp)
                print(f"Content: {skill_content}")
                doc.contents = skill_content
                doc.updated_at = skill["updated_at"]
                num_updats += 1
                print(f"******* skill {skill['id']} is updated *********")
        
        ## if skill does not exist, then add to db
        if not flag_doc_exists: 
            print(f"******* adding skill {skill['id']} *********")
            
            # ## transfer nested and parent skills to string
            # skill = skill_transformer(skill=skill, lst_skills=lst_skills)
        
            ## generate content for the skill
            temp = skill_lite(skill)
            skill_content = dict_content_generator(temp)
            print(f"Content: {skill_content}")
            pprint(skill)
            ## write skill to a document object
            new_doc = Document(
                entity_id = skill["id"],
                entity_id_full = f"sse/skill/{skill['id']}",
                entity_type = "skill",
                contents = skill_content,
                created_at = skill["created_at"],
                updated_at = skill["updated_at"]
            )
            # print('the new doc object')
            # pprint(schema_document.dump(new_doc))
            # result.append(schema_document.dump(new_doc))
            db.session.add(new_doc)
            num_adds += 1
            print(f"******* skill {skill['id']} added to databs *********")
    
    
    ## commit the changes to database
    db.session.commit()
        
    return num_adds, num_updats


def get_list_of_learning_paths():
    response = sse_learningpath_api.learning_path_mgmt_controller_get_learning_path()
    d = LearningPathListDto(skills=response.learningPaths)
    request_data = d.to_dict()
    list_of_learning_paths = request_data["learningPaths"]
    return list_of_learning_paths


def get_list_of_learning_units():
    response = sse_learningunit_api.search_learning_unit_controller_list_learning_units()
    data = SearchLearningUnitListDto(learning_units=response.learning_units)
    request_data = data.to_dict()
    list_of_learning_units = request_data["learning_units"]
    
    return list_of_learning_units


def transformer_list_of_learning_units(list_of_learning_units):
    new_list = []
    
    for learning_unit in list_of_learning_units:
        ## make a copy of the learning unit
        temp = learning_unit
        
        if learning_unit["teaching_goals"] != []:
            ## convert to skill names
            temp["teaching_goals"] = get_list_of_skill_names(learning_unit["teaching_goals"])
        
        if learning_unit["required_skills"] != []:
            ## convert to skill names
            temp["required_skills"] = get_list_of_skill_names(learning_unit["required_skills"])
        
        new_list.append(temp)
                
                
    return new_list


## given a list of skill-ids, get the list of skll-names
def get_list_of_skill_names(list_of_skill_ids):
    list_of_skills = get_list_of_skills()
    list_of_skill_names = []
    for sid in list_of_skill_ids:
        ns_item = next(item for item in list_of_skills if item["id"] == sid)
        list_of_skill_names.append(ns_item["name"])
        
    return list_of_skill_names


def db_task_updater(list_of_learning_units):
    num_adds = 0
    num_updates = 0
    
    for learning_unit in list_of_learning_units:
        ## get the contents from mls
        task_id = learning_unit["id"]
        
        ## check if task already exists 
        doc = Document.query.filter_by(entity_id=task_id, entity_type="task").first()
        
        flag_doc_exists = (doc!=None)
        flag_doc_is_modified = (doc.updated_at != learning_unit["updated_at"])
        
        if not flag_doc_exists:
            ## if the task does not exist, add to database
            ## get task content from MLS
            task_content = get_task_content(task_id)
            print(task_content)
            
            num_adds += 1
            

            
    
    return num_adds, num_updates



def db_learning_unit_processor(list_learning_units):
    for learning_unit in list_learning_units:
        
        ## get content for learning unit
        content = ""
        content = content + 'Title: ' + learning_unit.get('title') + "."
        content = content + learning_unit.get('description') + "."
        content = content + "Content creator is " + learning_unit.get('contentCreator') + "."
        content = content + "Content provider is " + learning_unit.get('contentProvider') + "."
        content = content + "Target audience is " + learning_unit.get('targetAudience') + "."
        content = content + "Content tags are " + ' '.join(learning_unit.get('contentTags')) + "."
        content = content + "Context tags are " + ' '.join(learning_unit.get('contextTags')) + "."
        ## write into document obj
        new_doc = Document(
            owner="", # owner == orga-id
            entity_id="", # entity_id == id
            entity_type="", # entity_type == {task, skill, path}
            contents="",
            language="", 
        )
        
        ## add to db
        db.session.add()
    db.session.commit()
    return