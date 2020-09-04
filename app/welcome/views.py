from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    message = "Hello, {}. You're at the izCert welcome page."
    if request.user.is_authenticated:
        message = message.format(request.user)
    else:
        message = message.format('world')
    template = loader.get_template('welcome/index.html')
    context = {
        'message': message,
        'user': request.user,
    }
    return HttpResponse(template.render(context, request))