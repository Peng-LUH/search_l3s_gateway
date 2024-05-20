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
    MLS_CONFIG,
    MLSConnection
)
from l3s_gateway_api import db
from l3s_gateway_api.models.task import Task
from l3s_gateway_api.models.document import Document
from .endpoints import ns_database

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


## --------------------------------- MLS ------------------------------------- ##
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
from swagger_client.sse_search_client.models.skill_dto import SkillDto
from swagger_client.sse_search_client.models.skill_list_dto import SkillListDto
from swagger_client.sse_search_client.models.search_learning_unit_list_dto import SearchLearningUnitListDto
from swagger_client.sse_search_client.models.learning_path_list_dto import LearningPathListDto

def skill_content_generator(skill_obj):
    # Convert the dictionary to a string representation
    dict_str = ', '.join([f"{key}: {value}" for key, value in skill_obj.items()])
    # print(dict_str)
    # Use the OpenAI API to generate a description
    messages = [
        {"role": "system", "content": "You are a teacher with 30 years of experience. You are designed to output JSON."},
        {"role": "user", "content": f"Please give me a summary about the skill with the provided information: {dict_str}. I want this explaination of this skill to be in German. The summary must contain the following information: the name of the skill, the description of the skill, the nested skills and parent skills. The output should be in one paragraph. The key must be 'Zusammenfassung'. This summary will be used as input of word embedding for semantic search algorithm."},
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
    description = description.replace('\n', '').replace('\r', '')
    if not description.endswith('"}'):
        description += '"}'
        
    summary = json.loads(description)
    content = list(summary.values())[0]
    return content

def get_list_of_skills():
    '''Get the list of skills'''
    response = sse_skill_api.skill_mgmt_controller_get_all_skills()
    d = SkillListDto(skills=response.skills)
    request_data = d.to_dict()
    # print(request_data.get("skills")[0])
    list_of_skills = request_data["skills"]
    sorted_list = sorted(list_of_skills, key=lambda x: x["id"])
    return sorted_list
    

## given a list of skill-ids, get the list of skll-names
def get_list_of_skill_names(list_of_skill_ids, list_of_skills):
    '''Given a list of skill-ids return the skill-names'''
    # list_of_skills = get_list_of_skills()
    list_of_skill_names = []
    for sid in list_of_skill_ids:
        ns_item = next(item for item in list_of_skills if item["id"] == sid)
        list_of_skill_names.append(ns_item["name"])
    return list_of_skill_names


from alive_progress import alive_bar
# from tqdm import tqdm
# from time import sleep
def transformer_list_of_skills(list_of_skills):
    '''convert the lsit of skills'''
    with alive_bar(len(list_of_skills)) as bar:
        new_list = []
        for skill in list_of_skills:
            skill = transformer_skill(skill, list_of_skills)
            new_list.append(skill)
            # ns_database.logger.info()
            bar()
            
    return new_list


def transformer_skill(skill, list_of_skills):
    if not skill["nested_skills"] == []:
        ns_names = get_list_of_skill_names(skill["nested_skills"], list_of_skills)
        
        # for ns in skill["nested_skills"]:
        #     ns_item = next(item for item in lst_skills if item["id"] == ns)
        #     ns_names.append(ns_item["name"])
        # print(ns_names)
        
        skill["nested_skills"] = ns_names
            
    if not skill["parent_skills"] == []:
        ps_names = get_list_of_skill_names(skill["parent_skills"], list_of_skills)
        
        # for ps in skill["parent_skills"]:
        #     ps_item = next(item for item in lst_skills if item["id"] == ps)
        #     ps_names.append(ps_item["name"])
        # print(ps_names)
        
        skill["parent_skills"] = ps_names
        
    return skill


def skill_lite(skill):
    '''create a lite version for content generation'''
    temp = copy.copy(skill)
    temp.pop('created_at', None)
    temp.pop('updated_at', None)
    temp.pop('id', None)
    temp.pop('repository_id', None)
    return temp


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
        print(f"Skill {skill['id']} already exists: {flag_doc_exists}")
        
        ## Case: skill already exists
        if flag_doc_exists:
            flag_doc_is_modified = not(doc.updated_at == skill["updated_at"])
            print(f"Is modified: {flag_doc_is_modified}")
            # check whether the skill is updated
            if not flag_doc_is_modified:
                print(f"*** skill {skill['id']} has no update")
                continue
            else: # write the info form skill to doc
                print(f"******* updating skill {skill['id']} *********")
                temp = skill_lite(skill)
                skill_content = skill_content_generator(temp)
                # print(f"Content: {skill_content}")
                
                doc.contents = skill_content
                doc.updated_at = skill["updated_at"]
                db.session.commit()
                print(f"******* skill {skill['id']} is updated *********")
                num_updats += 1
        
        ## Case: skill does not exist
        if not flag_doc_exists: 
            print(f"******* adding skill {skill['id']} *********")
            
            # ## transfer nested and parent skills to string
            # skill = transformer_skill(skill=skill, lst_skills=lst_skills)
        
            ## generate content for the skill
            temp = skill_lite(skill)
            skill_content = skill_content_generator(temp)
            # print(f"Content: {skill_content}")
            # pprint(skill)
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
            db.session.commit()
            print(f"******* skill {skill['id']} added to databs *********")
            num_adds += 1    
        
    return num_adds, num_updats


## ------------------------ Learning Path --------------------------- ##
def path_content_generator(path_obj):
    for key in path_obj.keys():
        if path_obj[key] == [] or path_obj[key] == None:
            path_obj[key] = 'None'
    # pprint(path_obj)
    
    # Convert the dictionary to a string representation
    dict_str = ', '.join([f"{key}: {value}" for key, value in path_obj.items()])
    # print(dict_str)
    
    # Use the OpenAI API to generate a description
    messages = [
        {"role": "system", "content": "You are a teacher with 30 years of experience. You are designed to output JSON."},
        {"role": "user", "content": f"Please give me a summary about the learning path with the provided information: '{dict_str}'.  The summary must contain the following information: the learning goals of this learning path, the recommended units from this learning path, and the requirements of this learning path. The output should be in one paragraph. I want this summary of this learning path to be in German. The key must be 'Zusammenfassung'. This summary will be used as input of word embedding for semantic search algorithm. The summary must be in complete sentences with less than 450 words."},
    ]
    
    # print(messages)
    # print(prompt)
    response = openai_client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
        response_format={ "type": "json_object" },
        max_tokens=500,  # Adjust the number of tokens as needed
    )
    
    # pprint(response)
    description = response.choices[0].message.content
    description = description.replace('\n', '').replace('\r', '')
    if not description.endswith('"}'):
        description += '"}'
        
    summary = json.loads(description)
    content = list(summary.values())[0]
    return content

def get_list_of_learning_paths():
    response = sse_learningpath_api.learning_path_mgmt_controller_get_learning_paths_of_owner()
    d = LearningPathListDto(learning_paths=response.learning_paths)
    request_data = d.to_dict()
    list_of_learning_paths = request_data["learning_paths"]
    sorted_list = sorted(list_of_learning_paths, key=lambda x: x["id"])
    return sorted_list


def transformer_path(path):
    ''''''
    try:
        requirements = []
        if path["requirements"] != []:
            for r in path["requirements"]:
                skill = sse_skill_api.skill_mgmt_controller_get_skill(skill_id=r)
                requirements.append(skill.name)
            
        path["requirements"] = requirements
        
        path_goals = []
        if path["path_goals"] != []:
            for g in path["path_goals"]:
                skill = sse_skill_api.skill_mgmt_controller_get_skill(skill_id=g)
                path_goals.append(skill.name)
        
        path["path_goals"] = path_goals
        
        
        recommended_unit_sequence = []
        if path["recommended_unit_sequence"] != []:
            for r in path["recommended_unit_sequence"]:
                learning_unit = sse_learningunit_api.search_learning_unit_controller_get_learning_unit(learning_unit_id=r)
                recommended_unit_sequence.append(learning_unit.title)
        
        path["recommended_unit_sequence"] = recommended_unit_sequence
        return path
    
    except KeyError as e:
        return e

def path_lite(path):
    temp = copy.copy(path)
    temp.pop('created_at', None)
    temp.pop('updated_at', None)
    temp.pop('id', None)
    temp.pop('lifecycle', None)
    temp.pop('owner', None)
    return temp

def transformer_list_of_paths(lst_of_paths):
    new_list = []
    for path in lst_of_paths:
        path = transformer_path(path)
        new_list.append(path)
        
    return new_list


def db_updater_paths(lst_of_paths):
    ## setup counter
    num_adds = 0
    num_updats = 0
    # result = []
    
    ## add skills to database
    for path in lst_of_paths:
        print(f"******* processing path {path['id']} *********")
        # check if the skill already exist in the db
        doc = Document.query.filter_by(entity_id=path["id"], entity_type="path").first()
        flag_doc_exists = (doc!=None)
        print(f"Already exists: {flag_doc_exists}")
        
        if flag_doc_exists:
            # check whether the skill is updated
            flag_doc_is_modified = not(doc.updated_at == path["updated_at"])
            print(f"Is modified: {flag_doc_is_modified}")
            
            if not flag_doc_is_modified:
                print(f"*** path {path['id']} already exists and has no update")
                continue
            else: # write the info form skill to doc
                print(f"******* updating path {path['id']} *********")
                temp = path_lite(path)
                path_content = path_content_generator(temp)
                # print(f"Content: {skill_content}")
                doc.contents = path_content
                doc.updated_at = path["updated_at"]
                print(f"******* path {path['id']} is updated *********")
                db.session.commit()
                num_updats += 1
                
        
        ## if path does not exist, then add to db
        if not flag_doc_exists: 
            print(f"******* adding path {path['id']} *********")
            
            # ## transfer nested and parent skills to string
            # skill = transformer_skill(skill=skill, lst_skills=lst_skills)
        
            ## generate content for the skill
            temp = path_lite(path)
            path_content = path_content_generator(temp)

            ## write path to a document object
            new_doc = Document(
                entity_id = path["id"],
                entity_id_full = f"sse/path/{path['id']}",
                entity_type = "path",
                contents = path_content,
                created_at = path["created_at"],
                updated_at = path["updated_at"]
            )
            # print('the new doc object')
            # pprint(schema_document.dump(new_doc))
            # result.append(schema_document.dump(new_doc))
            db.session.add(new_doc)
            db.session.commit()
            print(f"******* Path {path['id']} added to database *********")
            num_adds += 1
            
    
    
    ## commit the changes to database
    
        
    return num_adds, num_updats




## ------------------------ Tasks/Learning Units --------------------- ##
def get_list_of_tasks():
    response = sse_learningunit_api.search_learning_unit_controller_list_learning_units()
    data = SearchLearningUnitListDto(learning_units=response.learning_units)
    request_data = data.to_dict()
    list_of_learning_units = request_data["learning_units"]
    sorted_list = sorted(list_of_learning_units, key=lambda x: x["id"])
    return sorted_list


def transformer_list_of_tasks(list_of_tasks):
    new_list = []
    list_of_skills = get_list_of_skills()
    
    for task in list_of_tasks:
        ## make a copy of the learning unit
        temp = task
        
        if task['content_creator'] != []:
            ## TODO: get User-info
            temp['content_creator'] = task['content_creator']
        
        if task['content_provider'] != []:
            ## TODO: get content provider info
            temp['content_provider'] = task['content_provider']
        
        if task["teaching_goals"] != []:
            ## convert to skill names
            temp["teaching_goals"] = get_list_of_skill_names(list_of_skill_ids=task["teaching_goals"], list_of_skills=list_of_skills)
        
        if task["required_skills"] != []:
            ## convert to skill names
            temp["required_skills"] = get_list_of_skill_names(list_of_skill_ids=task["required_skills"], list_of_skills=list_of_skills)
        
        new_list.append(temp)
                
    return new_list


def list_of_task_lite(list_of_tasks):
    new_list = []
    for task in list_of_tasks:
        temp = {}
        temp["content_tags"] = task["content_tags"]
        temp['context_tags'] = task['context_tags']
        temp['description'] = task['description']
        temp['required_skills'] = task['required_skills']
        temp['target_audience'] = task['target_audience']
        temp['teaching_goals'] = task['teaching_goals']
        temp['title'] = task['title']
        temp['id'] = task['id']
        temp['content_creator'] = task['content_creator']
        temp['content_provider'] = task['content_provider']
        temp['semantic_density'] = task['semantic_density']
        temp['semantic_gravity'] = task['semantic_gravity']
        temp['created_at'] = task['created_at']
        temp['updated_at'] = task['updated_at']
        new_list.append(temp)
    return new_list


# def task_content_generator(path_obj):
#     for key in path_obj.keys():
#         if path_obj[key] == [] or path_obj[key] == None:
#             path_obj[key] = 'None'
#     # pprint(path_obj)
    
#     # Convert the dictionary to a string representation
#     dict_str = ', '.join([f"{key}: {value}" for key, value in path_obj.items()])
#     # print(dict_str)
    
#     # Use the OpenAI API to generate a description
#     messages = [
#         {"role": "system", "content": "You are a teacher with 30 years of experience. You are designed to output JSON."},
#         {"role": "user", "content": f"Please give me a summary about the learning path with the provided information: '{dict_str}'.  The summary must contain the following information: the learning goals of this learning path, the recommended units from this learning path, and the requirements of this learning path. The output should be in one paragraph. I want this summary of this learning path to be in German. The key must be 'Zusammenfassung'. This summary will be used as input of word embedding for semantic search algorithm. The summary must be in complete sentences."},
#     ]
    
#     # print(messages)
#     # print(prompt)
#     response = openai_client.chat.completions.create(
#         model="gpt-4-1106-preview",
#         messages=messages,
#         response_format={ "type": "json_object" },
#         max_tokens=300,  # Adjust the number of tokens as needed
#     )
    
#     # pprint(response)
#     description = response.choices[0].message.content
#     description = description.replace('\n', '').replace('\r', '')
#     if not description.endswith('"}'):
#         description += '"}'
        
#     summary = json.loads(description)
#     content = list(summary.values())[0]
#     return content


# def get_mls_task_content(task_id):
#     # new_list = []
#     # for task in list_of_tasks:
#     #     task_id = task['id']
#     #     mls_task_content = get_task_content_from_mls(task_id)
#     #     task['mls_content'] = mls_task_content
#     #     new_list.append(task)
#     mls_task_content = get_task_content_from_mls(task_id)
#     return mls_task_content


from l3s_gateway_api.util import mls_api
import re
from bs4 import BeautifulSoup

def get_task_content_from_mls(task_id):
    mls_response_json = mls_api.MLSConnection().get_task_by_id(task_id=task_id)
    # pprint(mls_response_json)
    mls_task_content = ""
    if mls_response_json['title'] != '':
        mls_task_content = mls_task_content + f"Title: {mls_response_json['title']}. "
    
    if mls_response_json['description'] != '':
        description_str = re.sub(r'</?p>', '', mls_response_json['description'])
        mls_task_content = mls_task_content + f'Description: {description_str}'
    
    if mls_response_json['taskSteps'] != []:
        for task_step in mls_response_json['taskSteps']:
            task_step_response = mls_api.MLSConnection().get_task_step_by_id(task_step_id=task_step)
            
            task_step_title = task_step_response['title']
            mls_task_content = mls_task_content + f'{task_step_title}. '
            
            task_step_content = BeautifulSoup(task_step_response['content'][0]['value'], 'html.parser').get_text()
            task_step_content = task_step_content.replace(u'\xa0', u'')
            task_step_content = task_step_content.replace(u'\n', u' ')
            mls_task_content = mls_task_content + f'{task_step_content}. '
    return mls_task_content


def db_learning_unit_updater(list_of_tasks):
    num_adds = 0
    num_updates = 0
        
    for task in list_of_tasks:
        ## get the contents from mls
        task_id = task["id"]
        
        ## check if task already exists 
        doc = Document.query.filter_by(entity_id=task_id, entity_type="task").first()
        
        flag_doc_exists = (doc!=None)
        print(f'flag_doc_exists : {flag_doc_exists}')
        
        if flag_doc_exists: ## if document already exists in db
            flag_doc_is_modified = (doc.updated_at != task["updated_at"])
            print(f'flag_doc_is_modified: {flag_doc_is_modified}')
        
            if not flag_doc_is_modified:
                print(f"*** task {task['id']} already exists and has no update")
                continue
            else: # write the info form skill to doc
                print(f"******* updating task {task['id']} *********")
                task_content = get_task_content(task=task)
                print(task_content)
                doc.contents = task_content
                doc.updated_at = task["updated_at"]
                print(f"******* path {task['id']} is updated *********")
                db.session.commit()
                num_updats += 1
                
        else: ## if the task does not exist, add to database
            ## get task content from MLS
            task_content = get_task_content(task)
            print(task_content)
             ## write into document obj
            new_doc = Document(
                    entity_id = task["id"],
                    entity_id_full = f"sse/learning_unit/{task['id']}",
                    entity_type = "task",
                    contents = task_content,
                    created_at = task["created_at"],
                    updated_at = task["updated_at"]
                )
            pprint(new_doc)
#            ## add to db
            db.session.add(new_doc)
            db.session.commit()
            num_adds += 1
            
    return num_adds, num_updates


def get_task_content(task):
    task_content = ''
    print('**************')
    pprint(task)
    if task['content_creator'] != '':
        task_content = task_content + f'Content Creator: {task["content_creator"]}. '
    if task['content_provider'] != '':
        task_content = task_content + f'Content Provider: {task["content_provider"]}. '
    if task['title'] != '':
        task_content = task_content + f'Title: {task["title"]}. '
    if task['description'] != '':
        task_content = task_content + f'Description: {task["description"]}. '
    if task['required_skills'] != []:
        task_content = task_content + f'Required Skills: {", ".join(task["required_skills"])}. '
    if task['teaching_goals'] != []:
        task_content = task_content + f'Teaching Goals: {", ".join(task["teaching_goals"])}. '
    if task['target_audience'] != []:
        task_content = task_content + f'Target Audience: {", ".join(task["target_audience"])}. '
    if task['content_tags'] != []:
        task_content = task_content + f'Content Tags: {", ".join(task["content_tags"])}. '
    if task['context_tags'] != []:
        task_content = task_content + f'Context Tags: {", ".join(task["context_tags"])}. '
    
    
    mls_task_content = get_task_content_from_mls(task['id'])
    task_content = task_content + f'{mls_task_content}'
    task_content = task_content.replace(u'..', u'.')
    task_content = task_content.replace(u'. .', u'.')
    
    task_content = task_content_compressor(task_content=task_content)
    return task_content


def task_content_compressor(task_content):
    
    messages = [
        {"role": "system", "content": "You are a teacher with 30 years of experience. You are designed to output JSON."},
        {"role": "user", "content": f"Please give me a summary about the task with the provided information: {task_content}. The summary is in German language. The length of this summary should not exceed 500 tokens."},
    ]
    # print(prompt)
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        response_format={ "type": "json_object" },
        max_tokens=512,  # Adjust the number of tokens as needed
    )
    # print(response)
    description = response.choices[0].message.content
    description = description.replace('\n', '').replace('\r', '')
    if not description.endswith('"}'):
        description += '"}'
        
    summary = json.loads(description)
    content = list(summary.values())[0]
    return content

# def db_learning_unit_processor(list_of_tasks):
#     for learning_unit in list_of_tasks:
        
#         ## get content for learning unit
#         content = ""
#         content = content + 'Title: ' + learning_unit.get('title') + "."
#         content = content + learning_unit.get('description') + "."
#         content = content + "Content creator is " + learning_unit.get('contentCreator') + "."
#         content = content + "Content provider is " + learning_unit.get('contentProvider') + "."
#         content = content + "Target audience is " + learning_unit.get('targetAudience') + "."
#         content = content + "Content tags are " + ' '.join(learning_unit.get('contentTags')) + "."
#         content = content + "Context tags are " + ' '.join(learning_unit.get('contextTags')) + "."
#         ## write into document obj
#         new_doc = Document(
#                 entity_id = learning_unit["id"],
#                 entity_id_full = f"sse/learning_unit/{learning_unit['id']}",
#                 entity_type = "path",
#                 contents = content,
#                 created_at = learning_unit["created_at"],
#                 updated_at = learning_unit["updated_at"]
#             )
        
#         ## add to db
#         db.session.add()
#     db.session.commit()
#     return

