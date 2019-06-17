from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.shortcuts import render

def index(request):
    a="""
    <center>
    <h1>绣春刀</h1>
    <h2>查看所有可疑人员</h2>
    <h2>添加可疑人员</h2>
    <h2>删除可疑人员</h2>
    </center>
    """
    return HttpResponse(a)
def findall(request):
    return HttpResponse('<center><h2 style="color:red">查看所有可疑人员</h1></center>')
def add(request):
    return HttpResponse('<center><h2 style="color:blue">添加可疑人员</h1></center>')
def delete(request):
    return HttpResponse('<center><h2 style="color:yellow">删除可疑人员</h1></center>')
# Create your views here.
