from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
import requests, json
import os, socket

from .dto import todo

ns_downstream = Namespace("downstream", validate=True, description="endpoints to reach the l3s-services")

# register dto models
# ns_downstream.models[search_srv_request_model.name] = search_srv_request_model
# ns_downstream.models[recsys_srv_request_model.name] = recsys_srv_request_model
ns_downstream.models[todo.name] = todo

@ns_downstream.route("/downstream/ok", endpoint="downstream_ok")
class DownstreamOk(Resource):
    @ns_downstream.response(int(HTTPStatus.CREATED), "successfully get.")
    @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
    @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
    @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
    def get(self):
        """Test the connection of downstream endpoints"""
        return {"message": "success"}, HTTPStatus.OK

#     @ns_downstream.response(int(HTTPStatus.CREATED), "successfully created.")
#     @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
#     @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
#     @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
#     @ns_downstream.expect(todo)
#     def post(self):
#         data = ns_downstream.payload
#         return data, HTTPStatus.CREATED

#     @ns_downstream.response(int(HTTPStatus.CREATED), "successfully changed.")
#     @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
#     @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
#     @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
#     @ns_downstream.expect(todo)
#     def put(self):
#         data = ns_downstream.payload
#         return data, HTTPStatus.ACCEPTED

#     @ns_downstream.response(int(HTTPStatus.CREATED), "successfully deleted.")
#     @ns_downstream.response(int(HTTPStatus.CONFLICT), "exits conflict.")
#     @ns_downstream.response(int(HTTPStatus.BAD_REQUEST), "validation error.")
#     @ns_downstream.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "internal server error.")
#     def delete(self):
#         return {"message": "delete method downstream"}, HTTPStatus.OK


## return ip address
@ns_downstream.route('/host-name-ip', endpoint="host_name_ip")
class Host(Resource):
    def get(self):
        HostName = os.getenv("HOST_NAME")
        IPAddr = os.getenv("HOST_IP")
        return {"Host IP": IPAddr}, HTTPStatus.OK



## check accessibility of l3s-services
@ns_downstream.route('/check-up', endpoint="check_up")
class CheckUp(Resource):
    def get(self):
        l3s_servies_ports = ["L3S_AIMETA_PORT", "L3S_RECSYS_PORT", "L3S_SEARCH_PORT"]
        # l3s_servies_ports = ["L3S_SEARCH_PORT"]
        result = {}
        
        for port in l3s_servies_ports:
            url = f'http://{os.getenv("HOST_IP")}:{os.getenv(port)}'
            
            try:
                response = requests.head(url)
                if response.status_code == 200:
                    result.update({port: 'success'})
                else:
                    result.update({port: 'failed'})
            except requests.ConnectionError as e:
                result.update({port: e.errno})
            
        return result, HTTPStatus.OK
                

@ns_downstream.route('/test')
class Test(Resource):
    def get(self):
        # current_ip = os.getenv("HOST_IP")
        l3s_search_port = os.getenv("L3S_SEARCH_PORT")
        response = requests.get(f"http://localhost:{l3s_search_port}/l3s-search/search-metadata/get-datasets")
        return response.json()



    
    

