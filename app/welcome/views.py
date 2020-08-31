from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    message = "Hello, world. You're at the izCert welcome page."
    template = loader.get_template('welcome/index.html')
    context = {
        'message': message,
    }
    return HttpResponse(template.render(context, request))