from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    # ex: /courses/
    path('', views.index, name='index'),

    # ex: /courses/coursename
    path('<str:url_name>', views.detail, name='detail'),
]