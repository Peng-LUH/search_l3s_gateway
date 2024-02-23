from l3s_gateway_api import ma

from l3s_gateway_api.models.test import Test

# class TestsSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = Test
    
#     id = ma.auto_field()
#     public_id = ma.auto_field()
#     entity_type = ma.auto_field()
#     firstList = ma.auto_field()
#     secondList = ma.auto_field()
#     created_at = ma.auto_field()
#     modified_at = ma.auto_field()
#     this_id = ma.auto_field()

class TestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Test
    
    id = ma.auto_field()
    # public_id = ma.auto_field()
    entity_type = ma.auto_field()
    firstList = ma.auto_field()
    secondList = ma.auto_field()
    created_at = ma.auto_field()
    modified_at = ma.auto_field()
    this_id = ma.auto_field()


from l3s_gateway_api.models.task import Task
class TaskSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Task
    
    task_id = ma.auto_field()
    task_id_full = ma.auto_field()
    entity_type = ma.auto_field()
    created_on = ma.auto_field()
    modified_on = ma.auto_field()
    
    
from l3s_gateway_api.models.document import Document
class DocumentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Document
        
    # id = ma.auto_field()
    entity_id = ma.auto_field()
    entity_type = ma.auto_field()
    entity_id_full = ma.auto_field()
    owner = ma.auto_field()
    contents = ma.auto_field()
    
    # created_at = ma.auto_field()
    # updated_at = ma.auto_field()
    
    