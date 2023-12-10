from l3s_gateway_api import ma

from l3s_gateway_api.models.document import Document
class DocumentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Document
        
    id = ma.auto_field()
    owner = ma.auto_field()
    entity_id = ma.auto_field()
    entity_id_full = ma.auto_field()
    entity_type = ma.auto_field()
    contents = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()