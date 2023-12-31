from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    mobile = models.CharField(verbose_name="手机", max_length=11)


class Department(models.Model):
    title = models.CharField(verbose_name="部门名称", max_length=32)


class User(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    depart = models.ForeignKey(verbose_name="关联部门", to=Department, on_delete=models.CASCADE)
