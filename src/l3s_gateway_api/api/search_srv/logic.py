from dotenv import load_dotenv
load_dotenv()


from flask import jsonify, request

from swagger_client import l3s_search_client
# from swagger_client_L3S import l3s_recsys_client as l3SSearchClient
import dataclasses, json
from pprint import pprint
from swagger_client.l3s_search_client.rest import ApiException
import os

from swagger_client.l3s_search_client.models.dense_search_response import DenseSearchResponse
from swagger_client.l3s_search_client.models.dense_search_request import DenseSearchRequest
from swagger_client.l3s_search_client.models.dense_search_response_list import DenseSearchResponseList
# from swagger_client_L3S.l3s_search_client.models.random_response import RandomResponse
# from swagger_client_L3S.l3s_search_client.models.random_request import RandomRequest


## Configuration L3S Recsys
l3s_search_config = l3s_search_client.Configuration()
l3s_search_config.host = "http://localhost:9043/l3s-search/"
# l3s_search_config.host = os.getenv('L3S_SEARCH_HOST')
# print(l3s_recsys_config.host)


client_l3s_search = l3s_search_client.ApiClient(configuration=l3s_search_config)
# l3s recsys api registration
search_searcher_api = l3s_search_client.SearcherApi(api_client=client_l3s_search)
# recsys_random_api = l3s_search_client.RandomApi(api_client=client_l3s_search)


def searchDenseRetrieval(request_data):
    # request_data = request.get_json()
    
    try:
    # Get list of exposure types
        print(search_searcher_api.api_client.configuration.host)
        api_response = search_searcher_api.post_dense_retrieval(body=request_data)
        print(api_response)
        # print(len(api_response))
        print(type(api_response))
        # pprint(api_response)
        
        d = DenseSearchResponseList(results=api_response.results)
        response = jsonify(d.to_dict())
        response.status_code = 201
        return response
       
    except ApiException as e:
       
        return ("Exception when calling Api-> %s\n" % e)
    
    
