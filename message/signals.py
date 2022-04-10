from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import send_mail
from app.settings import EMAIL_HOST_USER

from message.models import Message


@receiver(post_save, sender=Message)
def NotifyMe(sender, instance, created, *args, **kwargs):
    if created:
        pass
        # message = f'{instance.email} sent you a message. {instance.message}'
        # send_mail("PORTFOLIO NEW MESSAGE", message,
        #           EMAIL_HOST_USER, ["chineduie01@gmail.com"])
