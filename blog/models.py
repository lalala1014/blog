from django.db import models
from tinymce.models import HTMLField

class users_manage(models.Manager):
    def create_user(self,username,pwd,email,phone):
        self.create(username = username ,pwd = pwd,email = email,phone = phone)
        print("创建成功")
    def delete_user(self,id):
        self.filter(id=id).delete()
    def update_user(self,id,age,email,phone,head,sex):
        self.filter(id=id).update(age=age,email=email,phone=phone,head=head,sex=sex)
    def select_user(self,username):
        user = self.filter(username=username)
        return user

class text_manage(models.Manager):
    def create_text(self,title,content,author_id):
        self.create(title=title,content=content,author_id=author_id)
    def delete_text(self,title_id):
        self.filter(id=title_id).delete()
    def update_text(self,title_id,title,content):
        self.filter(id=title_id).update(title=title,content=content)
    def select_text(self,title):
        user = self.filter(title=title)
        return user
# Create your models here.
#注意继承Model父类，来给数据库映射起来
class users(models.Model): # 用户类
    id = models.AutoField(primary_key = True) # 主键 自增
    username = models.CharField(max_length = 20 ,null=False, blank = False,unique = True) # 注意字符串给到长度限制
    pwd = models.CharField(max_length = 32 , default = "12345678")  # 整型 默认值18
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=11,null=True)
    sex = models.CharField(default="男", max_length=3, null=False)
    age = models.IntegerField(verbose_name="年龄", default=18, null=False)
    head = models.ImageField(upload_to="static/blog/userimg/",default="/static/blog/userimg/default.jpg")

    Users_manage = users_manage()  # 第二种方法 类管理器
    def __str__(self):
        return self.username

class text(models.Model):   # 文章类
    id = models.AutoField(primary_key=True)  # 主键 自增
    author = models.ForeignKey(users,models.CASCADE)
    title = models.CharField(blank = False,max_length = 20)
    time = models.DateTimeField(verbose_name="修改时间",auto_now =True)
    # content = models.CharField(max_length = 400)
    text_manage = text_manage()
    content = HTMLField()

    def __str__(self):
        return "author:" + str(self.author) +" title:"+str(self.title)





