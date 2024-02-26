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



dto_completion_task_summary_response_item = Model("DtoCompletionTaskSummaryResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "summary": fields.String(description='Summary of the given task', example="""In dieser Lerneinheit steht der Schlitten im Fokus. 
                             Du wirst lernen, deine Ziele zu definieren, 
                             die Funktion des Bauteils zu verstehen und einen genauen Arbeitsplan zu erstellen. 
                             Dabei ist es wichtig, Form- und Lagetoleranzen einzuhalten und Sicherheitsvorschriften zu beachten. 
                             Nachdem du den Schlitten hergestellt hast, 
                             kannst du deine Arbeit reflektieren und deine Ergebnisse mit deinem Lernbegleiter besprechen. 
                             Um deine Fortschritte festzuhalten, füllst du die \"Ich kann ...\"-Listen für überfachliche und fachliche Kompetenzen aus. 
                             Lade deine Ergebnisse in deine Notizen hoch. 
                             Ganz wichtig: 
                             Du kannst die bereits heruntergeladenen Listen und Bewertungsbögen weiterbearbeiten und musst keine neuen anlegen, 
                             um deinen Lernfortschritt besser nachverfolgen zu können. 
                             Diese Lerneinheit ist eine spannende Herausforderung für dich, 
                             also plane und arbeite sorgfältig und effektiv, um den Schlitten in optimaler Qualität herzustellen. Viel Erfolg!""")
                        })



dto_completion_task_summary_response = Model('DtoCompletionTaskSummaryResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested( dto_completion_task_summary_response_item, description='Results')
                                        })




dto_completion_title_response_item = Model("DtoCompletionTitleResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "title": fields.List(fields.String, description='List of Titles for given task', example=[
    "Informiere dich über den Schlitten",
    "Plane den Bau des Schlittens",
    "Erstelle einen Arbeitsplan für den Schlittenbau"
  ])
})


dto_completion_title_response = Model('DtoCompletionTitleResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_completion_title_response_item, description='Results')
                                        })




dto_completion_content_tags_response_item = Model("DtoCompletionContentTagsResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "content_tags": fields.List(fields.String, description='List of Content Tags', example=[
    "Arbeitsauftrag",
    "Ziele",
    "Funktion",
    "Bauteil",
    "Einzelteilzeichnung",
    "anspruchsvolles Werkstück",
    "Arbeitsfolge",
    "Form- und Lagetoleranzen",
    "Arbeitsplan"
  ])
})


dto_completion_content_tags_response = Model('DtoCompletionContentTagsResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_completion_content_tags_response_item, description='Results')
                                        })



dto_completion_context_tags_response_item = Model("DtoCompletionContextTagsResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "context_tags": fields.List(fields.String, description='List of Context Tags', example=["Arbeitsplanung", "Herstellung", "Reflexion", "Erfolgskontrolle"
                                                                                            ])
})




dto_completion_context_tags_response = Model('DtoCompletionContextTagsResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_completion_context_tags_response_item, description='Results')
                                        })



dto_completion_new_existing_skills_response_item = Model("DtoCompletionNewExistingSkillsResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "new_skills": fields.List(fields.String, description='List of new skills in the learning task', example=                            
                                                                        [
                                                                          "Zielsetzung und Selbstreflexion",
                                                                          "Effektive Planung",
                                                                          "Praktische Umsetzung",
                                                                          "Beobachtung und Reflexion",
                                                                          "Erfolgskontrolle"
                                                                        ]),
    "existing_skills": fields.List(fields.String, description='List of existing skills ids for the learning task', example=[
    "1",
    "2",
    "3"])                                                              

})



dto_completion_new_existing_skills_response = Model('DtoCompletionNewExistingSkillsResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_completion_new_existing_skills_response_item, description='Results')
                                        })






completion_quiz_item = Model('DtoCompletionQuizItem', {
    'wissen': fields.List(fields.String, description='List of Wissen quiz questions',example =[
      "Welche Fragen sollen in der Reflexion besprochen werden?",
      "Welche Sicherheitsvorschriften sollten bei der Herstellung beachtet werden?"
    ]),
    'verstehen': fields.List(fields.String, description='List of Verstehen quiz questions', example = [
      "Was sind die Ziele bei der Herstellung des Schlittens?",
      "Was ist die Funktion des Bauteils?"
    ]),
    'anwenden': fields.List(fields.String, description='List of Anwenden quiz questions', example = [
      "Wie kannst du eine Arbeitsfolge planen, um die geforderten Toleranzen einzuhalten?",
      "Wie kannst du den Arbeitsplan ausformulieren, um den Schlitten in optimaler Qualität herzustellen?"
    ]),
})

dto_completion_quiz_questions_response_item = Model("DtoCompletionQuizQuestionsResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "quiz_questions": fields.Nested(completion_quiz_item, description='Quiz questions categorized by taxonomy level')

})


<<<<<<< HEAD
dto_aimeta_course_summary = Model("DtoAimetaCourseSummary", {
    "task_id": fields.String(),
    "summary": fields.String()
})

dto_aimeta_course_summary_response = Model("DtoAimetaCourseSummaryResponse", {
    "message": fields.String(),
    "results": fields.Nested(dto_aimeta_course_summary)
})
=======
dto_completion_quiz_questions_response = Model('DtoCompletionQuizQuestionsResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_completion_quiz_questions_response_item, description='Results')
                                        })


dto_completion_learning_goal_response_item = Model("DtoCompletionLearningGoalResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "learning_goals": fields.List(fields.String, description='List of learning goals', example=[
        "Die Funktion des Bauteils 'Schlitten' verstehen",
        "Einen effektiven Arbeitsplan für die Herstellung des Schlittens erstellen",
        "Den Schlitten sicher und effektiv herstellen und dabei Form- und Lagetoleranzen einhalten"
    ])
})


dto_completion_learning_goal_response = Model('DtoCompletionLearningGoalResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_completion_learning_goal_response_item, description='Results')
                                        })
>>>>>>> ebc085ac2e497beb2b7e5986f671123b931ecedf
