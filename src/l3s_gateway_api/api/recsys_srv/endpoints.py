## import libraries
from flask import request, jsonify
from flask_restx import Namespace, Resource, fields, reqparse
from http import HTTPStatus
import requests, json
import os, socket
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

print(os.getenv('L3S_RECSYS_HOST'))
l3s_recsys_config.host = os.getenv('L3S_RECSYS_HOST')
# print("")
print('l3s_recsys_config.host:', l3s_recsys_config.host)

client_l3s_recsys = l3s_recsys_client.ApiClient(configuration=l3s_recsys_config)
# l3s recsys api registration
recsys_test_api = l3s_recsys_client.TestApi(api_client=client_l3s_recsys)
recsys_random_api = l3s_recsys_client.RandomApi(api_client=client_l3s_recsys)


ns_recsys_srv = Namespace("Recsys Service", validate=True, description="downstream endpoints for recsys services")


@ns_recsys_srv.route('/test/ok', endpoint="recsys_service_ok")
class RecommendationService(Resource):
    @ns_recsys_srv.response(int(HTTPStatus.CREATED), "successfully changed.")
    @ns_recsys_srv.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_recsys_srv.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_recsys_srv.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def get(self):
        return {"message": "success"}, HTTPStatus.OK


get_n_random_rec_parser = reqparse.RequestParser()
get_n_random_rec_parser.add_argument('num_of_rec', type=int, location='args', default=10)

@ns_recsys_srv.route('/random/get-n-random-recommendation')
class GetNRandomRecommendation(Resource):
    @ns_recsys_srv.expect(get_n_random_rec_parser)
    def get(self):
        args=get_n_random_rec_parser.parse_args()
        # print("args=parser.parse_args()")
        # print(dict(args))
        request_data = dict(args)
    
        try:
        # Get list of exposure types
            print(recsys_random_api.api_client.configuration.host)
            api_response = recsys_random_api.post_random_recommendation(body=request_data)
            
            print('tpye of api_response:', type(api_response))            

            d = RandomResponse(results=api_response.results)
            response = jsonify(d.to_dict())
            response.status_code = 200
            return response
        
        except ApiException as e:
        
            return ("Exception when calling Api-> %s\n" % e)