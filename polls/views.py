
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PollSerializer, PollAnswerSerializer, PollQuestionSerializer
from .models import Poll, PollAnswer, PollQuestion
from . import serializers

import urllib.request


class PollsManager(APIView):
    """ Processor of all requests from the client by API """

    # curl --location --request GET 'http://localhost:8000/api/active_polls/'
    def get(self, request, *args, **kwargs):
        polls = Poll.objects.all()
        if len(polls) > 0:
            serializer = PollSerializer(polls, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'error',
                'data': 'An error occurred during serialization of current polls'
            }, status=status.HTTP_400_BAD_REQUEST)


class AnswersList(APIView):
    """ User answer handler """

    # curl --location --request GET 'http://localhost:8000/api/answers_polls/'
    def get(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        answers = PollAnswer.objects.filter(user_id=user_id)
        if len(answers) > 0:
            serializer = PollAnswerSerializer(answers, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'status': 'error',
                'data': 'No answers were found for this ID'
            }, status=status.HTTP_400_BAD_REQUEST)

class AnswerCreater(APIView):
    """ User answer handler """

    # curl --location --request POST 'http://localhost:8000/api/active_polls/{id}/'
    def post(self, request, *args, **kwargs):
        question_id = request.data.get('question_id')
        user_id = request.data.get('user_id')
        answer_id = request.data.get('answer_id')
        answer_text = request.data.get('answer_text')

        # Check if the question exists in the database
        if PollQuestion.objects.filter(id = question_id).exists():
            data = {
                'question_poll': question_id,
                'user_id' : user_id,
                'answer_id': answer_id,
                'answer_text' : answer_text,
            }
            serializer = PollAnswerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status': 'error',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': 'error',
                'data': 'Invalid Question ID'
            }, status=status.HTTP_400_BAD_REQUEST)
