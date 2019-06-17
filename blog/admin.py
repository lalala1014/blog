from django.contrib import admin
from . import models
class UserAdmin(admin.ModelAdmin):
    # 列表页面要显示属性
    list_display = ["username","sex","age","email","phone"]
    # 过滤器[按照什么过滤]
    list_filter = ["sex"]
# Register your models here.
admin.site.register(models.text)
admin.site.register(models.users,UserAdmin)

