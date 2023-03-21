from flask_restx import Model, fields
from search_l3s_gateway.api.upstream import ns_upstream

### test_model
test_model = ns_upstream.model(
    "Testing", {
        "input_1": fields.String,
        "input_2": fields.String,
        "input_3": fields.List(fields.String),
        "input_4": fields.String,
    }
)

### service_model
service_model = ns_upstream.model(
    "Service", {
        "user_id": fields.String(required=False, description="The user ID in MLS"),
        "org_id": fields.String(required=False, description="The organization's ID in MLS"),
        "service_type": fields.String(required=True, description="The requesting service type."),
        "content": fields.String(required=True, description="The content to be processed."),
    }
)

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


request_model = ns_upstream.model('Request', {
    'user_id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

retrieve_model = ns_upstream.model(
    "Retrieve", {
        "data": fields.String,
    }
)