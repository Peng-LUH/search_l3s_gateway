from l3s_recsys import l3s_recsys_client
import os
from flask import jsonify

configuration = l3s_recsys_client.Configuration()
configuration.host = os.getenv('L3S_RECSYS_HOST')
api_client = l3s_recsys_client.ApiClient(configuration=configuration)
api_instance = l3s_recsys_client.TestApi(api_client=api_client)


def recsys_test():
    print("l3s-recsys/ok")
    print(api_instance.api_client.configuration.host)
    api_response = api_instance.get_recsys_test()
    print(str(api_response))
    
    

    