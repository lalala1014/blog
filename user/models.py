from django.db import models
from tinymce.models import HTMLField

content = HTMLField()
class users_manage(models.Manager):
    def create_user(self,name,age):
        self.create(name = name ,age = age)
        return "create successful"
    def delete_user(self,id):
        self.filter(id=id).delete()
        return "delete successful"
    def update_user(self,id,name,age):
        self.filter(id=id).update(name=name,age=age)
        return "update successful"
    def select_user(self,id):
        user = self.filter(id=id)
        return user
# Create your models here.
#注意继承Model父类，来给数据库映射起来
class users(models.Model):
    id = models.AutoField(primary_key = True) # 主键 自增
    name = models.CharField(max_length = 50) # 注意字符串给到长度限制
    age = models.IntegerField(default=18)  # 整型 默认值18
    Users_manage = users_manage()  # 第二种方法 类管理器

    # @classmethod
    # def create(cls,name):
    #     author = cls(name = name)
    #     return author

    def __str__(self):
        return "name:" + str(self.name) +" age:"+str(self.age)


