#!/bin/bash
root=./src/swagger_client
client_name=l3s_search_client
json_file=json_file/l3s_search_api.json
json_file_dir=$root/$json_file
dir=$root/client
swagger-codegen generate -i $json_file_dir -l python -o $dir -DpackageName=$client_name
sudo rm -r -f $root/$client_name
sudo mv $dir/$client_name $root
sudo rm -r -f $dir