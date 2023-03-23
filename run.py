import os

from search_l3s_gateway import create_app
from search_l3s_gateway import db
from search_l3s_gateway.models.user import User

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {"db": db, "User": User}
