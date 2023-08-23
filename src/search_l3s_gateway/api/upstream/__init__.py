from flask_restx import Namespace
ns_upstream = Namespace("upstream", validate=True, description="endpoints to communicate with the mls")