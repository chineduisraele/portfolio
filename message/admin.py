from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Message


# Register your models here.
class MessageAdmin(ModelAdmin):
    list_display = ('email', 'name', 'time', 'read')
    ordering = ('read',)


admin.site.register(Message, MessageAdmin)
