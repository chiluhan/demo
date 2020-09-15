from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField('书名',max_length=20)
    price=models.DecimalField('定价',decimal_places=2,max_digits=5)
    maker_price=models.DecimalField('市场价',decimal_places=2,max_digits=5, default=0.0)
    pub=models.CharField('出版社',max_length=50,default='')

    def __str__(self):
        return '%s-%s-%s-%s-%s'%(self.title,self.price,self.pub,self.maker_price,self.pub)

    class Meta:
        db_table='book'

class Author(models.Model):
    name=models.CharField('姓名',max_length=10)
    age=models.IntegerField('年龄',default=18)
    email=models.EmailField('邮箱',null=True)