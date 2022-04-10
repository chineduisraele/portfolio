
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Message

# Create your views here.


@csrf_exempt
def MessageView(request, *args, **kwargs):

    if request.method == "POST":
        data = request.POST
        newMessage = Message.objects.create(
            name=data['name'], email=data['email'], phone=data['phone'], message=data['message'])
        newMessage.save()
        return HttpResponse('created', status=200)
