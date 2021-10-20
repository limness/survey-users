from django.contrib import admin

from .models import Poll, PollQuestion, PollAnswer


class ItemAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['data_begin']
        return []

admin.site.register(Poll, ItemAdmin)
admin.site.register(PollQuestion)
