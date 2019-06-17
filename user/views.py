
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from .Form import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
def index(request):
    a="""
    <center>
        <h1>功能大全</h1>
        <a href="/user/create" style="color=red">增加</h2>
        <a href="/user/delete" style="color=blue">删除</h2>
        <a href="/user/update" style="color=yellow">更改</h2>
        <a href="/user/select" style="color=green">查找</h2>
    </center>
    """
    # return HttpResponse(a)
    return redirect("lalala:index2")
def create_user(request):
    result = models.users.Users_manage.create_user("yuyuyu",90) # 增加
    return HttpResponse(result)
def update_user(request):
    result = models.users.Users_manage.update_user(4,"lalala",17) # 更新
    return HttpResponse(result)
def delete_user(request):
    result = models.users.Users_manage.delete_user(2) # 删除
    return HttpResponse(result)
def select_user(request):
    result = models.users.Users_manage.select_user(1) # 查找
    return HttpResponse(result)

# 第一个参数就是正则分组的参数
def param1(request,name):
    print("前端传输的name：",name)
    return HttpResponse("这个是使用位置参数方式")

# 这个是使用命名参数
def param2(request,jerry):
    print("前端传输的username:",jerry)
    print("path:",request.path)
    print("cookies:",request.COOKIES)
    print("GET:",request.GET)
    print("encoding",request.encoding)
    # print("request:",dir(request))
    return HttpResponse("这个是使用命名参数方式")

def index2(request):
    temp = loader.get_template("user/login.html")
    context = {"user":"lalala"}
    return HttpResponse(temp.render(context,request))

def index3(request):
    if request.method=="POST":
        name = request.POST.get("user")
        print(name)
    user = models.users.Users_manage.get(pk=4)
    student = models.users.Users_manage.all()
    print(student)
    return render(request,"user/login.html",{"user":user,"student":student})

def login_success(request):
    return render(request,"user/login_success.html")

def regist_success(request):
    return render(request,"user/regist_success.html")

def login(request):
    return render(request,"user/login.html")

def regist(request):
    return render(request,"user/register.html")

def index4(request):
    return HttpResponse("lalalalalalalala")

@csrf_exempt #跨站请求伪造
def test(request):
    user = models.users.Users_manage.get(pk=123)
    request.session["user"] = serialize("json", user)
    if request.method == "GET":
        return render(request, "user/test.html")
    elif request.method == "POST":
        res = {}
        res["data"] = {"name": "哈哈"}
        users = models.users.Users_manage.all()
        # users = serialize("json",users)
        return HttpResponse(users)


def test2(request):
    form = UserForm()
    if request.method == "GET":
        return render(request,"/user/test.html",{"form":form})
    elif request.method == "POST":
        return render(request,"/user/test2.html",{"form":form,"msg":"登陆成功！"})
