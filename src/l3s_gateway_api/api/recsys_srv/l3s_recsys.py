

import os
from flask import jsonify, request
import dataclasses, json
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()


from swagger_client_L3S import l3s_recsys_client
from swagger_client_L3S.l3s_recsys_client.rest import ApiException
from swagger_client_L3S.l3s_recsys_client.models.test import Test as TestDto
from swagger_client_L3S.l3s_recsys_client.models.random_response import RandomResponse
from swagger_client_L3S.l3s_recsys_client.models.random_request import RandomRequest


## Configuration L3S Recsys
l3s_recsys_config = l3s_recsys_client.Configuration()
# l3s_recsys_config.host = "https://staging.sse.uni-hildesheim.de:9042/l3s-recsys/"
l3s_recsys_config.host = os.getenv('L3S_RECSYS_HOST')
# print(l3s_recsys_config.host)

client_l3s_recsys = l3s_recsys_client.ApiClient(configuration=l3s_recsys_config)
# l3s recsys api registration
recsys_test_api = l3s_recsys_client.TestApi(api_client=client_l3s_recsys)
recsys_random_api = l3s_recsys_client.RandomApi(api_client=client_l3s_recsys)



def recsysTestGet():
    try:
    # Get list of exposure types
        print(recsys_test_api.api_client.configuration.host)
        api_response = recsys_test_api.get_recsys_test()
        print(api_response)
        pprint(api_response)
        
        d = TestDto(message=api_response.message)
        response = jsonify(d.to_dict())
        response.status_code = 200
        return response
       
    except ApiException as e:
       
        return ("Exception when calling Api-> %s\n" % e)



def recsysTestPost():
    
    request_data = request.get_json()
    
    try:
    # Get list of exposure types
        print(recsys_test_api.api_client.configuration.host)
        api_response = recsys_test_api.post_recsys_test(request_data)
        print(api_response)
        print(type(api_response))
        # pprint(api_response)
        
        d = TestDto(message=api_response.message)
        response = jsonify(d.to_dict())
        response.status_code = 201
        return response
       
    except ApiException as e:
       
        return ("Exception when calling Api-> %s\n" % e)



def recsysRandom():
    request_data = request.get_json()
    print(request_data)
    try:
    # Get list of exposure types
        print(recsys_random_api.api_client.configuration.host)
        api_response = recsys_random_api.post_random_recommendation(body=request_data)
        print(api_response)
        print(type(api_response))
        # pprint(api_response)
        
        d = RandomResponse(id=api_response.id)
        response = jsonify(d.to_dict())
        response.status_code = 200
        return response
       
    except ApiException as e:
       
        return ("Exception when calling Api-> %s\n" % e)


# def testUP():

#     configuration = l3SClient.Configuration()
#     configuration.host = os.getenv('L3S_GATEWAY')
#     api_client = l3SClient.ApiClient(configuration=configuration)
#     api_instance_up = l3SClient.UpstreamApi(api_client=api_client)

#     configuration = l3SSearchClient.Configuration()
#     configuration.host = os.getenv('L3S_GATEWAY')
#     api_client = l3SSearchClient.ApiClient(configuration=configuration)
    
#     try:
#     # Get list of exposure types
#         print(api_instance_up.api_client.configuration.host)
#         api_response = api_instance_up.get_test_upstream()
#         print(api_response)
#         pprint(api_response)
        
#         return api_response
       
#     except ApiException as e:
       
#         return ("Exception when calling Api-> %s\n" % e)




# def testDown():

#     configuration = l3SClient.Configuration()
#     configuration.host = os.getenv('L3S_GATEWAY')
#     api_client = l3SClient.ApiClient(configuration=configuration)
    
#     api_instance_down = l3SClient.DownstreamApi(api_client=api_client)
    
#     try:
#     # Get list of exposure types
#         print(api_instance_down.api_client.configuration.host)
#         api_response = api_instance_down.get_test_upstream()
#         print(api_response)
#         pprint(api_response)
        
#         return api_response
       
#     except ApiException as e:
       
#         return ("Exception when calling Api-> %s\n" % e)



    
