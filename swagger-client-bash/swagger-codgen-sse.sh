#!/bin/bash
root=./src/swagger_client
client_name=sse_search_client
json_file=json_file/sse_search_api.json
json_file_dir=$root/$json_file
dir=$root/client
swagger-codegen generate -i $json_file_dir -l python -o $dir -DpackageName=$client_name
sudo rm -r -f $root/$client_name
sudo mv $dir/$client_name $root
sudo rm -r -f $dir

##https://staging.sse.uni-hildesheim.de:9011/api-json