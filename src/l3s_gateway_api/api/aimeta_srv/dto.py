from flask_restx import fields, Model

dto_completion_task_response = Model("DtoCompletionTaskResponse", {
    "unit_id": fields.String(),
    "existing_skills": fields.List(fields.String(), description="list of skill ids"),
    "new_skills": fields.List(fields.String(), description="list of skill ids"),
    "title": fields.String(),
    "summary": fields.String(),
    "content_tags": fields.List(fields.String()),
    "context_tags": fields.List(fields.String())
})

dto_aimeta_connection_response = Model("DtoAimetaConnectionResponse", {
    "host_url": fields.String(),
    "status": fields.String()
})

# dto_completion_unit_response = Model("DtoCompletionUnitResponse", {
#     "unit_id": fields.String(),
#     "request_type": fields.String(),
#     "value": fields.List(fields.String())
# })

dto_completion_task_title_response = Model("DtoCompletionTaskTitleResponse", {
    "unit_id": fields.String(),
    "title": fields.String()
})

dto_completion_task_summary_response = Model("DtoCompletionTaskSummaryResponse", {
    "unit_id": fields.String(),
    "summary": fields.String()
})

dto_completion_task_content_tags_response = Model("DtoCompletionTaskContentTagsResponse", {
    "unit_id": fields.String(),
    "content_tags": fields.List(fields.String())
})

dto_completion_task_context_tags_response = Model("DtoCompletionTaskContextTagsResponse", {
    "unit_id": fields.String(),
    "context_tags": fields.List(fields.String())
})

dto_completion_task_quiz_questions_response = Model("DtoCompletionTaskQuizQuestionsResponse", {
    "unit_id": fields.String(),
    "quiz_questions": fields.List(fields.String())
})

dto_completion_task_taught_skills_response = Model("DtoCompletionTaskTaughtSkillsResponse", {
    "unit_id": fields.String(),
    "new_skills": fields.List(fields.String()),
    "existing_skills": fields.List(fields.String())
})
