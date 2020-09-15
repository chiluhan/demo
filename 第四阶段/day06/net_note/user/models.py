from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=20,unique=True)
    #保存口令的Hash值,如果选择md5,Hash值长度是128位
    #长度为32,是32个16进制字符,1个16进制是4位,正好32*4=128
    password=models.CharField(max_length=32)
    create_time=models.DateTimeField(auto_now_add=True)
    updata_time=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username