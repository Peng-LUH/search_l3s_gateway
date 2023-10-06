from flask_restx import Model, fields

dto_recommendation_object = Model("DtoRecommendationObj", {
    "type": fields.String(description="the object is either a skill, path or unit"),
    "id": fields.String(description="ID of a task, path or skill")
})

dto_get_recommendation_reponse = Model("DtoGetRecommendationReponse", {
    "results": fields.List(fields.Nested(dto_recommendation_object))
})