from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=18,min_length=5,label="用户名称")
    password = forms.CharField(max_length=18,min_length=5,label="用户密码")