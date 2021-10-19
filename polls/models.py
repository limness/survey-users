from django.db import models


class Poll(models.Model):
    """Poll"""
    poll_name = models.CharField(max_length=200)
    description = models.CharField(default='', max_length=150)
    data_begin = models.DateField()
    data_end = models.DateField()

    def __str__(self):
       return str(self.poll_name)

class PollQuestion(models.Model):
    """Poll questions"""

    QUESTION_CHOICES = [
        ('own_asnwer', 'own_asnwer'),
        ('choices_answer', 'choices_answer'),
    ]

    poll = models.ForeignKey(Poll,
                             on_delete=models.CASCADE,
                             related_name='questions',
                             blank=True,
                             null=True,
                             default=None)
    question_type = models.CharField(max_length=30,
                                     choices=QUESTION_CHOICES,
                                     default="own_asnwer",
                                     blank=True)
    question_text = models.CharField(max_length=250)

    def __str__(self):
       return str(self.question_text)

class PollAnswer(models.Model):
    """Response options from users"""
    question_poll = models.ForeignKey(PollQuestion,
                             on_delete=models.CASCADE,
                             related_name='answer',
                             blank=True,
                             null=True,
                             default=None)
    user_id = models.IntegerField()
    answer_id = models.CharField(default=0, max_length=2)
    answer_text = models.CharField(default='', max_length=10)

    def __str__(self):
       return str(self.id)
