from django.urls import path

from . import views

app_name = "forum"

urlpatterns = [
    # List all questions
    path("questions/", views.QuestionListView.as_view(), name="question_list"),
    # View a single question along with its answers
    path(
        "question/<int:pk>/", views.QuestionDetailView.as_view(), name="question_detail"
    ),
    # Create a new question
    path(
        "question/create/", views.QuestionCreateView.as_view(), name="question_create"
    ),
    # Create an answer for a specific question
    path(
        "question/<int:pk>/answer/",
        views.AnswerCreateView.as_view(),
        name="answer_create",
    ),
    path("question/<int:pk>/delete/", views.delete_question, name="delete_question"),
    # Like or unlike an answer
    path("answer/<int:pk>/like/", views.like_answer, name="like_answer"),
]
