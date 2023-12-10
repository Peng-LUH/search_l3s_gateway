from l3s_gateway_api import db
from uuid import uuid4

from sqlalchemy.types import ARRAY, String
from sqlalchemy.sql import func, text
from l3s_gateway_api.util.datetime_util import (
    utc_now,
    get_local_utcoffset,
    make_tzaware,
    localized_dt_string,
)


func.gen_pid = lambda: str(uuid4())

class Task(db.Model):
    """model for storing details of the task."""

    __tablename__ = "Task"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # public_id = db.Column(db.String(36), unique=True, server_default=func.gen_pid()) # public id in l3s
    owner = db.Column(db.String(), default=None, nullable=True)
    creator = db.Column(db.String(), default=None, nullable=True)
    task_id = db.Column(db.Integer, unique=True) # the id in mls/sse
    task_id_full = db.Column(db.String(255), unique=True)
    entity_type = db.Column(db.String(100), nullable=False, server_default="task")
    title = db.Column(db.String(256), unique=True, nullable=True)
    description = db.Column(db.String(1024), nullable=True)
    contents = db.Column(db.String(), nullable=True)
    context_tags = db.Column(ARRAY(String), nullable=True)
    content_tags = db.Column(ARRAY(String), nullable=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    modified_on = db.Column(db.DateTime, server_default=func.now())
    
    
    def __repr__(self):
        return (
            f'''<User task_id={self.task_id_full},
            entity_type={self.entity_type},
            created_on={self.created_on}
            '''
        )
    
    @classmethod
    def find_by_owner(cls, owner):
        return db.session.execute(db.select(cls).filter_by(owner=owner)).all()

    @classmethod
    def find_by_creator(cls, creator):
        return db.session.execute(db.select(cls).filter_by(creator=creator)).all()
    
    @classmethod
    def find_by_task_id(cls, task_id):
        return db.session.execute(db.select(cls).filter_by(task_id=task_id)).first()
    
    @classmethod
    def find_by_task_id_full(cls, task_id_full):
        return db.session.execute(db.select(cls).filter_by(task_id_full=task_id_full)).first()
    
    @classmethod
    def find_by_entity_type(cls, entity_type):
        return db.session.execute(db.select(cls).filter_by(entity_type=entity_type)).all()