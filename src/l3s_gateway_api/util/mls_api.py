import os
import json, requests
from pprint import pprint



class MLS_CONFIG(object):
    MLS_BASE_URL=os.getenv('MLS_BASE_URL')
    MLS_LOGIN_SERVER_URL=os.getenv('MLS_LOGIN_SERVER_URL')
    MLS_REALM=os.getenv('MLS_REALM')
    MLS_CLIENT_ID=os.getenv('MLS_CLIENT_ID')
    MLS_CLIENT_SECRET=os.getenv('MLS_CLIENT_SECRET')
    MLS_USERNAME=os.getenv('MLS_USERNAME')
    MLS_USER_PASSWORD=os.getenv('MLS_USER_PASSWORD')
    MLS_GRANT_TYPE=os.getenv('MLS_GRANT_TYPE')
    MLS_LOGIN_PAYLOAD = {
    "client_id": os.getenv("MLS_CLIENT_ID"),
    "client_secret": os.getenv("MLS_CLIENT_SECRET"),
    "username": os.getenv("MLS_USERNAME"),
    "password": os.getenv("MLS_USER_PASSWORD"),
    "grant_type": os.getenv("MLS_GRANT_TYPE"),
    }
    

class MLSConnection(object):
    def __get_login_response(self):
        """returns response as json object"""
        login_server_url = MLS_CONFIG.MLS_LOGIN_SERVER_URL
        realm = MLS_CONFIG.MLS_REALM
        login_payload = MLS_CONFIG.MLS_LOGIN_PAYLOAD
        
        login_response = requests.post(login_server_url + "/realms/" + realm + "/protocol/openid-connect/token",
                data = login_payload,
                headers =  {
                "Content-Type": "application/x-www-form-urlencoded",
                }
            )
        return login_response
    
    def __get_access_token(self):
        login_response = self.__get_login_response()
        return login_response.json()["access_token"]
    
    def __get_auth_header(self):
        access_token = self.__get_access_token()
        accept_header="application/ld+json"
        auth_header =  {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
            "accept": accept_header,
            }
        return auth_header
    
    def __get_response(self, base_url, content_type, auth_header):
        url = base_url+"/mls-api/"+content_type
        response = requests.get(url, headers=auth_header)
        
        return response
    
    def get_task_by_id(self, task_id):
        base_url = MLS_CONFIG.MLS_BASE_URL
        auth_header = self.__get_auth_header()
        
        target_url = base_url + f"/mls-api/tasks/{task_id}"
        
        task_id_response = requests.get(target_url, headers = auth_header)
        # pprint(task_id_response)
        # pprint(task_id_response.status_code)
        return task_id_response
    
    def get_task_step_by_id(self, task_step_id):
        """
        Retrieves the details of a task step by its ID from the MLS system.

        Parameters:
        ----------
        task_step_id : str
            The ID of the task step to retrieve.

        Returns:
        -------
        dict
            A dictionary containing the details of the task step.
        """
        base_url = MLS_CONFIG.MLS_BASE_URL  # Base URL for the MLS system
        auth_header = self.__get_auth_header()  # Authentication header for the request
        
        # Construct the target URL by appending the task step ID to the base URL
        target_url = base_url + task_step_id
        
        # Make a GET request to the target URL with the authentication header
        task_step_id_response = requests.get(target_url, headers=auth_header)
        
        # Return the JSON response as a dictionary
        return task_step_id_response.json()