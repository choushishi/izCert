from django.urls import path

from . import views

app_name = 'register'
urlpatterns = [
    # ex: /courses/
    path('', views.register, name='register'),

]