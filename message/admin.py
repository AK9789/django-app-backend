from django.contrib import admin

# Register your models here.

from .models import Message
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'sendedBy',
    )

admin.site.register(Message, MessageAdmin)

from .models import Requests
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email'
    )

admin.site.register(Requests, RequestAdmin)