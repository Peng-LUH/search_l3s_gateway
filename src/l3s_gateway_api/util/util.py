from flask import request
import urllib


# aaa = urllib.parse.urlparse('http://127.0.0.1:9040/l3s-gateway/l3s-search/init/learning-units')

# import requests

def get_request_url(endpoint_url):
    # r1 = request.base_url.rsplit('/', 3)[0]
    parse_base_url = urllib.parse.urlparse(request.base_url)
    if endpoint_url[0] == '/':
        endpoint_url = endpoint_url[1:]
    request_url = f"{parse_base_url.scheme}://{parse_base_url.netloc}/{endpoint_url}"
    return request_url