from django.conf.urls import url

from . import views

app_name = 'welcome'
urlpatterns = [
    url('', views.index, name='index'),
]