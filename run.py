import os

from l3s_gateway_api import create_app
from l3s_gateway_api import db
# from l3s_gateway_api.models.user import User

app = create_app(os.getenv("FLASK_ENV", "development"))

# with app.app_context():
#     db.create_all()

@app.shell_context_processor
def shell():
    return {"db": db}
