from django.conf.urls import url
from hire import views


urlpattern = [
        url(r'^$', views.index, name='index'),
        ]