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

def course(request, url_name):
    template = loader.get_template('courses/course.html')
    course = Course.objects.get(url_name__exact=url_name)
    sessions = course.get_sessions()
    context = {
        'course': course,
        'sessions': sessions,
    }
    return HttpResponse(template.render(context, request))

def lecture(request, course_url_name, lecture_url_name):
    template = loader.get_template('courses/lecture.html')
    course = Course.objects.get(url_name__exact=course_url_name)
    lecture = LectureSession.objects.get(url_name__exact=lecture_url_name)
    previous_lecture, next_lecture = course.get_prv_and_next_session(lecture_url_name)
    context = {
        'course': course,
        'lecture': lecture,
        'previous_lecture': previous_lecture,
        'next_lecture': next_lecture,
    }
    return HttpResponse(template.render(context, request))