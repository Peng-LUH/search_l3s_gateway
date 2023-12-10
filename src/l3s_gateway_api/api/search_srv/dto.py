from flask_restx import Model, fields


# todo = Model('Todo', {
#     'id': fields.Integer(readonly=True, description='The task unique identifier'),
#     'task': fields.String(required=True, description='The task details')
# })

search_srv_request_model = Model('Search_Srv_Request', {
    "uid": fields.String(description="user ID", default=None),
    "cid": fields.String(description="company ID", default=None),
    "query": fields.String(required=True, default="Elektrotechnik 1 Versuch 8: Wirkleistung von Wechselspannungen; Wirkleistung der Sinuswechselspannung in der praktischen \u00dcbung"),
    "language_model": fields.String(default="bert-base-german-cased"),
    "index_method": fields.String(default="flat-l2"),
    "dataset_name": fields.String(default="mls-tasks-full"),
    "nr_result": fields.Integer(min=1, default=10)
})

recsys_srv_request_model = Model('Recsys_Srv_Request', {
    "uid": fields.String(description="user ID", default=None),
    "cid": fields.String(description="company ID", default=None),
    "catetory": fields.String(description="recsys category", default=None)
})


model_search_srv_connection_response = Model('DtoSearchSrvConnectionResponse', {
    "host_url": fields.String(),
    "status": fields.String()
})


model_get_dataset_response = Model('DtoGetDatasetResponse', {
    "message": fields.String(),
    "results": fields.List(fields.String())
})

dto_unit_search_response = Model('DtoUnitSearchResponse', {
    'unit_ids': fields.List(fields.String(), description = 'List of unit ids')
})


dto_search_response = Model("DtoSearchResponse", {
    "user_id": fields.String(description="user ID", default=None),
    "owner": fields.String(description="company ID", default=None),
    "entity_id": fields.String(),
    "entity_type": fields.String(),
    "similarity": fields.Float()
})

dto_search_response_list = Model("DtoSearchResponseList",{
    "message": fields.String(),
    "results": fields.List(fields.Nested(dto_search_response)),
})