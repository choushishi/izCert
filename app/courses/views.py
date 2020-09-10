from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Course, LectureSession

# Create your views here.
def index(request):
    template = loader.get_template('courses/index.html')
    courses = [c.get_template_representation() for c in Course.objects.all()]

    context = {
        'subscribed_course_list': courses
    }
    return HttpResponse(template.render(context, request))

def detail(request, url_name):
    template = loader.get_template('courses/detail.html')
    course = Course.objects.get(url_name__exact=url_name)
    sessions = course.lecturesession_set.all()
    context = {
        'course': course,
        'sessions': sessions,
    }
    return HttpResponse(template.render(context, request))