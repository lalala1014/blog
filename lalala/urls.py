from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^findall/$', views.findall),
    url(r'^add/$', views.add),
    url(r'^delete/$', views.delete),
]