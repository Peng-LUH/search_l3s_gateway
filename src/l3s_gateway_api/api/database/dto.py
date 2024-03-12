from flask_restx import Model, fields
from l3s_gateway_api.util import fields as customFields

### test_model
test_model = Model(
    "Testing", {
        "input_1": fields.String,
        "input_2": fields.String,
        "input_3": fields.List(fields.String),
        "input_4": fields.String,
    }
)

### service_model
service_model = Model(
    "Service", {
        "user_id": fields.String(required=False, description="The user ID in MLS"),
        "org_id": fields.String(required=False, description="The organization's ID in MLS"),
        "service_type": fields.String(required=True, description="The requesting service type."),
        "content": fields.String(required=True, description="The content to be processed."),
    }
)

dto_sse_connection_response = Model("DtoSSEConnectionResponse", {
    "host_url": fields.String(),
    "status": fields.String()
})
# service_reqparser = RequestParser(bundle_errors=True)
# service_reqparser.add_argument(
#     name="user_id", type=str, location="form",
# )
# service_reqparser.add_argument(
#     name="org_id", type=str, location="form",
# )
# service_reqparser.add_argument(
#     name="service_type", type=str, location="form"
# )
# service_reqparser.add_argument(
#     name="content", type=str, location="form",
# )


request_model = Model('Request', {
    'user_id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

retrieve_model = Model(
    "Retrieve", {
        "data": fields.String,
    }
)
dto_test_request = Model('DtoTestRequest', {
    "firstList": fields.List(fields.String()),
    "secondList": fields.List(fields.String())
})

dto_test_response = Model('DtoTestResponse', {
    "id": fields.String(),
    "firstList": fields.List(fields.String()),
    "secondList": fields.List(fields.String())
})



dto_task_request = Model('DtoTaskRequest', {
    # 'title': fields.String(),
    # 'description': fields.String(),
    'contents': fields.String(),
    # 'entity_type': fields.String(),
    # 'context_tags': fields.List(fields.String()),
    # 'content_tags': fields.List(fields.String()),
    # 'owner': fields.String(),
    # 'entity_id': fields.String()
})

class RequestMethod(fields.String):
    # __schema_type__ = ["add", "modify", "delete"]
    # __schema_example__ = "'add' or 'modify' or 'delte'"
    def format(self, value):
        if value not in ["add", "modify", "delete"]:
            raise ValueError("invalid method")


## ------------------------ Document --------------------- ##
dto_document_delete_response = Model("DtoDocumentDeleteResponse", {
    "message": fields.String()
})



## ------------------------- Skill ------------------------ ##

dto_skill = Model("DtoSkill", {
    "name": fields.String(),
    "level": fields.Float(),
    "description": customFields.NullableString(),
    "id": fields.String(),
    "nestedSkills": fields.List(fields.String()),
    "parentSkills": fields.List(fields.String()),
    "repositoryId": fields.String(),
    "created_at": fields.String(),
    "updated_at": fields.String()
})

dto_skill_list = Model("DtoUpdateSkillsRequest", {
    # 'skill_ids': fields.List(fields.String(), description="skill ids"),
    # 'method': fields.String(description="add or modify or delete")
    "skills": fields.List(fields.Nested(dto_skill))
})


dto_sync_results = Model("DtoSkillsSyncResults", {
    "num_adds": fields.Integer(min=0),
    "num_updates": fields.Integer(min=0)
})

dto_sync_response = Model("DtoSyncSkillsResponse", {
    "message": fields.String(),
    "results": fields.Nested(dto_sync_results)
})

dto_sync = Model("DtoSync", {
    "entity_type": fields.String(),
    "message": fields.String(),
    "results": fields.Nested(dto_sync_results),
    "status_code": fields.Integer()
})

dto_sync_list = Model("DtoSyncList", {
    "sync_results": fields.List(fields.Nested(dto_sync))
})
## ------------------- Learning Path --------------------- ##

dto_update_paths_request = Model("DtoUpdatePathsRequest", {
    'path_ids': fields.List(fields.String(), description="skill ids"),
    'method': fields.String(description="add or modify or delete")
})


## ------------------ Learning Units --------------------##

dto_learning_unit = Model("DtoLearningUnit", {
    "teachingGoals": fields.List(fields.String()),
      "requiredSkills": fields.List(fields.String()),
      "id": fields.String(),
      "title": fields.String(),
      "language": fields.String(),
      "description": fields.String(),
      "processingTime": fields.String(),
      "rating": fields.String(),
      "contentCreator": fields.String(),
      "contentProvider": fields.String(),
      "targetAudience": fields.String(),
      "semanticDensity": fields.String(),
      "semanticGravity": fields.String(),
      "contentTags": fields.List(fields.String()),
      "contextTags": fields.List(fields.String()),
      "lifecycle": fields.String(),
      "orga_id": fields.String()
})

dto_init_learning_units_request = Model("DtoInitLearningUnitsRequest", {
    'learning_units': fields.List(fields.Nested(dto_learning_unit))
})


dto_l3s_events_request = Model('DtoSearchEventsRequest', {
    "entity_type": fields.String(default='task', required=True),
    "task_id": fields.String(required=True, description='task-id'),
    "method": fields.String(required=True, enum=["delete", "put", "post"], description='http methods')
})


dto_document_post_request = Model('DtoDocumentPostRequest', {
    'owner': fields.List(fields.String()),
    'contents': fields.String(),
    'created_at': fields.String(),
    'updated_at': fields.String()
})