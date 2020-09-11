from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    # ex: /courses/
    path('', views.index, name='index'),

    # ex: /courses/coursename
    path('<str:url_name>', views.course, name='course'),

    # ex: /courses/coursename/lecturename
    path('<str:course_url_name>/<str:lecture_url_name>', views.lecture, name='lecture')

]