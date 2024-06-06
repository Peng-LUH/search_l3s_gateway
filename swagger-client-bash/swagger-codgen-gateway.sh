#!/bin/bash
root=./src/swagger_client
client_name=l3s_gateway_client
json_file=json_file/l3s_gateway_api.json
json_file_dir=$root/$json_file
dir=$root/client
swagger-codegen generate -i $json_file_dir -l python -o $dir -DpackageName=$client_name
rm -r -f $root/$client_name
mv $dir/$client_name $root
rm -r -f $dir