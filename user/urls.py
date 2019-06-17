from django.conf.urls import url
from . import views

app_name = "lalala"
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create/$', views.create_user),
    url(r'^delete/$', views.delete_user),
    url(r'^update/$', views.update_user),
    url(r'^select/$', views.select_user),
    url(r'^(?P<jerry>\w+)/param2$',views.param2,name="param2"),
    url(r'^(\w+)/param1',views.param1,name="tom"),
    url(r'^index2/$',views.index2,name="index2"),
    url(r'^index3/$',views.index3),
    url(r'^login_success/$',views.login_success),
    url(r'^login/$',views.login,name="login"),
    url(r'^regist/$',views.regist),
    url(r'^regist_success/$',views.regist_success),
    url(r'^index4/$',views.index4),
    url(r'^test/$',views.test),
    url(r'^test2/$',views.test2),
]
