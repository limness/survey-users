
from django.urls import path
from . import views
from .views import PollsManager, AnswerCreater, AnswersList


urlpatterns = [
    path('active_polls/', PollsManager.as_view()),
    path('active_polls/<int:pk>/', AnswerCreater.as_view()),
    path('answers_polls/', AnswersList.as_view()),
]
