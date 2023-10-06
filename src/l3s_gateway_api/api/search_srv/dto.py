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
    "results": fields.List(fields.String())
})


dto_unit_search_response = Model('DtoUnitSearchResponse', {
    'unit_ids': fields.List(fields.String(), description = 'List of unit ids')
})


dto_search_events_request = Model('DtoSearchEventsRequest', {
    "entity_type": fields.String(default='task', required=True),
    "id": fields.String(required=True, description='task id'),
    "method": fields.String(required=True, description='http methods')
})

dto_search_events_response = Model('DtoSearchEventsResponse', {
    
})