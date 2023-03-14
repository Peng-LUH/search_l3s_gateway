from flask_restx.reqparse import RequestParser


service_reqparser = RequestParser(bundle_errors=True)
service_reqparser.add_argument(
    name="user_id", type=str, location="form",
)
service_reqparser.add_argument(
    name="org_id", type=str, location="form",
)
service_reqparser.add_argument(
    name="service_type", type=str, location="form"
)
service_reqparser.add_argument(
    name="content", type=str, location="form",
)