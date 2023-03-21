import os
import json, requests

MLS_LOGIN_PAYLOAD = {
  "client_id": os.getenv("MLS_CLIENT_ID"),
  "client_secret": os.getenv("MLS_CLIENT_SECRET"),
  "username": os.getenv("MLS_USERNAME"),
  "password": os.getenv("MLS_PASSWORD"),
  "grant_type": os.getenv("MLS_GRANT_TYPE"),
}


class MLSConnection(object):
    def get_login_response(self, login_server_url, realm, login_payload):
        """returns response as json object"""
        login_response = requests.post(login_server_url + "/realms/" + realm + "/protocol/openid-connect/token",
                data = login_payload,
                headers =  {
                "Content-Type": "application/x-www-form-urlencoded",
                }
            )
        return login_response.json()
    
    def get_access_token(self, login_response): 
        return login_response.json()["access_token"]
    
    def get_auth_header(self, access_token):
        auth_header =  {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json"
            }
        return auth_header
    
    def get_response(self, base_url, content_type, auth_header):
        url = base_url+"/mls-api/"+content_type
        print(url)
        tasks_response = requests.get(url, headers=auth_header)
        
        return tasks_response