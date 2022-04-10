from pyexpat import model
from django.db import models

# Create your models here.


class Message(models.Model):

    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.PositiveSmallIntegerField(blank=True, null=True)
    message = models.TextField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.email
