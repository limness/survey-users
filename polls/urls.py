
from django.urls import path
from . import views
from .views import PollsManager, AnswerCreater, AnswersList


urlpatterns = [
    path('active_polls/', PollsManager.as_view()),
    path('add_answer/', AnswerCreater.as_view()),
    path('answers_polls/', AnswersList.as_view()),
]
