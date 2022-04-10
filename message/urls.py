from email import message
from django.urls import path
from .views import MessageView

urlpatterns = [
    path('', MessageView, "")]
