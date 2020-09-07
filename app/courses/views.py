from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Course

# Create your views here.
def index(request):
    template = loader.get_template('courses/index.html')
    context = {
        'subscribed_course_list': Course.objects.all()
    }
    return HttpResponse(template.render(context, request))

def detail(request, url_name):
    template = loader.get_template('courses/detail.html')
    course = Course.objects.get(url_name__exact=url_name)
    context = {
        'course': course
    }
    return HttpResponse(template.render(context, request))