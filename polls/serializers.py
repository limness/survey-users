
from rest_framework import serializers
from .models import Poll, PollAnswer, PollQuestion


class PollQuestionSerializer(serializers.ModelSerializer):
    #poll_detail = PollSerializer(source='poll', read_only=True)
    question_type = serializers.CharField(max_length=30, default='own_asnwer')
    question_text = serializers.CharField(max_length=250)

    class Meta:
        model = PollQuestion
        fields = ('__all__')#('id', 'question_type', 'question_text')

class PollSerializer(serializers.ModelSerializer):
    poll_name = serializers.CharField(max_length=200, allow_blank=True)
    description = serializers.CharField(default='', max_length=150)
    questions = PollQuestionSerializer(many=True, read_only=True)
    data_begin = serializers.DateField()
    data_end = serializers.DateField()

    class Meta:
        model = Poll
        fields = ('__all__')

class PollAnswerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    answer_id = serializers.CharField(default=0, max_length=2)
    answer_text = serializers.CharField(default='', max_length=10)
    question_detail = PollQuestionSerializer(source='question_poll', read_only=True)

    class Meta:
        model = PollAnswer
        fields = ('__all__')
