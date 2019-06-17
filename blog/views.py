from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from io import BytesIO
from . import utils
import os
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required # 设置登录状态 暂时用不到
from django.core.cache import cache # 使用缓存



@csrf_exempt #跨站请求伪造
def login(request):  # 登录
    usera = models.users.Users_manage.all()
    text = models.text.text_manage.all()
    user = serialize("json", usera)
    user = json.loads(user)
    code = request.session['check_code']
    ajaxdic = {"code": code, "user": user}
    ajaxdic = json.dumps(ajaxdic)
    if request.method=="POST":
        #         if pwd == i.pwd :
        #             if request.session['check_code'] == check:
        #                 request.session["user_id"] = i.id
        #                 return render(request, "blog/login_success.html",{"text":text,"author":i.id})
        #             else:return HttpResponse("验证码错误！")
        # else:
        return HttpResponse(ajaxdic)
        # return render(request, "blog/login.html", {"user": user})
        # return HttpResponse("123")
    elif request.method == "GET":
        return render(request,"blog/login.html",{"user":ajaxdic})


# @login_required(login_url="blog:login")
def login_success(request,user_id):  # 登陆成功 可查询文章 创建新文章
    text = models.text.text_manage.all()
    user_id = int(user_id)
    user = models.users.Users_manage.get(id=user_id)
    request.session["user"] = user
    if request.method == "POST":
        return render(request,"blog/login_success.html",{"user":request.session["user"],"text":text})
    return render(request, "blog/login_success.html", {"user":request.session["user"],"text":text})

def text_content(request,title_id): # 查看文章内容
    text = models.text.text_manage.all()
    title_id = int(title_id)
    content=""
    title_name=""
    for j in text:
        if str(j.id) == str(title_id):
            request.session["book"] = j
    return render(request, "blog/text_content.html", {"author": request.session["user"], "book": request.session["book"]})

@csrf_exempt
def regist(request): # 注册 成功转到注册成功页面
    users = models.users.Users_manage.all()
    isRegist = "1"
    if request.method=="POST":
        print("13")
        name = request.POST.get("name")
        pwd = request.POST.get("pwd")
        email = request.POST.get("email")
        phone = request.POST.get("tel")
        for i in users:
            if name == i.username:
                isRegist = "0"
        if isRegist == "1":
            models.users.Users_manage.create_user(name,pwd,email,phone)
        return JsonResponse({"isRegist":isRegist})
    return render(request,"blog/register.html")

def delete(request,title_id):
    text = models.text.text_manage.all()
    # 删除文章
    models.text.text_manage.delete_text(title_id)
    return render(request, "blog/login_success.html", {"user": request.session["user"], "text": text})

#TODO
def update(request):
    if request.method == "POST":
        title = request.POST.get("title")
        print(title)
        content = request.POST.get("content")
        print(content)
        # 修改文章
        models.text.text_manage.update_text(int(request.session["title_id"]),str(title),str(content))
    return redirect("blog:login_success")

def create_code_img(request):
    # 在内存中开辟空间用以生成临时的图片
    f = BytesIO()
    img, code = utils.create_code()
    # 保存验证码信息到 session 中，方便下次表单提交时进行验证操作
    request.session['check_code'] = code
    img.save(f, 'PNG')
    return HttpResponse(f.getvalue())

# 修改用户个人资料
def update_user(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        sex = request.POST.get("sex")
        age = request.POST.get("age")
        try:
            head = request.FILES["header"]
            print(head.name)
            # head_path = os.path.join("static/blog/userimg/",head.name)
            # print(head_path)
            # with open(head_path,"wb") as f:
            #     for chunk in head.chunks():
            #         f.write(chunk)
            print(head)
            print(type(head))
        except:
            head = request.session["user"].head
        # path = default_storage.save("static/blog/userimg/"+head.name,Content)
        models.users.Users_manage.update_user(request.session["user"].id,age,email,phone,head,sex)
        return render(request,"blog/update_user.html",{"user":request.session["user"]})
        # return redirect("blog:update_user")
    return render(request, "blog/update_user.html",{"user":request.session["user"]})




# 测试专用
def test(request):
    if request.method == "POST":
        print(request.POST)
        head = request.FILES["header"]
        sex = request.POST.get("sex")
        print(head)
        print(sex)
        # path = default_storage.save("static/blog/userimg/"+head.name,Content)
        return render(request,"blog/update_user.html")
    return render(request, "blog/update_user.html")

