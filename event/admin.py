from django.contrib import admin
from .models import Event, Tech, PostScreen, PostRes


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Tech)
admin.site.register(PostScreen)
admin.site.register(PostRes)
