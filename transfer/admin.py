from django.contrib import admin

# Register your models here.
from .models import History

class historyadmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'attach', 
        'amount', 
        'sent_type'
    )

admin.site.register(History, historyadmin)