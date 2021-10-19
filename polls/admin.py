from django.contrib import admin

from .models import Poll, PollQuestion, PollAnswer


admin.site.register(Poll)
admin.site.register(PollQuestion)
admin.site.register(PollAnswer)
