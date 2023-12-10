"""Class definition for User model."""
from datetime import datetime, timezone, timedelta
from uuid import uuid4

import jwt
from flask import current_app
from l3s_gateway_api import db, bcrypt

from l3s_gateway_api.util.datetime_util import (
    utc_now,
    get_local_utcoffset,
    make_tzaware,
    localized_dt_string,
)
from sqlalchemy.ext.hybrid import hybrid_property
from l3s_gateway_api.util.result import Result
from sqlalchemy.types import ARRAY, PickleType, String
from sqlalchemy.sql import func
from sqlalchemy import text


func.pid = lambda: str(uuid4())

class Test(db.Model):

    __tablename__ = "test"
        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # public_id = db.Column(db.String(256), default=lambda: str(uuid4()))
    entity_type = db.Column(db.String(256), server_default="GEN")
    firstList = db.Column(ARRAY(String), nullable=True)
    secondList = db.Column(ARRAY(String), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    modified_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    this_id = db.Column(db.String(256), server_default=func.pid())

    def __repr__(self):
        return (
            f"<User id={self.id}, first_list={self.firstList}, second_list={self.secondList}>"
        )
    
    @classmethod
    def find_by_id(cls, id):
        return db.session.execute(db.select(cls).filter_by(id=id)).first()