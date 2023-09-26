import os
from l3s_gateway_api.util.mls_api import (
    MLS_LOGIN_PAYLOAD,
    MLSConnection
)

MLS_BASE_URL = os.getenv("MLS_BASE_URL")
MLS_LOGIN_SERVER_URL = os.getenv("MLS_LOGIN_SERVER_URL")
MLS_REALM = os.getenv("MLS_REALM")

def get_mls_content(content_type="documents", accept_header=None):
    
    c = MLSConnection()

    login_response = c.get_login_response(
        login_server_url=MLS_LOGIN_SERVER_URL,
        realm=MLS_REALM,
        login_payload=MLS_LOGIN_PAYLOAD
        )
    
    access_token = c.get_access_token(login_response)
    
    MLS_AUTH_HEADER = c.get_auth_header(access_token, accept_header)
    
    response = c.get_response(
        base_url=MLS_BASE_URL,
        content_type=content_type, 
        auth_header=MLS_AUTH_HEADER
        )
    return response