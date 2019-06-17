from django.conf.urls import url
from django.views.static import serve
from . import views
from homework import settings

app_name = "blog"
urlpatterns = [
    url(r'^login/$', views.login,name="login"), # 登录界面
    url(r'^login_success/(\d+)/$',views.login_success,name="login_success"), # 登陆成功的首页
    url(r'^regist/$',views.regist,name="regist"), # 注册界面
    url(r'^text_content/(\d+)/$',views.text_content,name="text_content"), # 查看文章界面
    url(r'^delete/(\d+)/$',views.delete,name="delete"),
    url(r'^update/$',views.update,name="update"),
    url(r'^code/$',views.create_code_img), # 创建验证码
    url(r'^update_user/$',views.update_user,name="update_user"),
    url(r'^test/$',views.test), # 测试专用
]
