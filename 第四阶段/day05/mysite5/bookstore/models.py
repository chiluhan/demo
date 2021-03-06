from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField('书名',max_length=20)
    price=models.DecimalField("定价",max_digits=5,decimal_places=2)
    market_price=models.DecimalField('零售价',max_digits=5,decimal_places=2)
    pub=models.CharField('出版社',max_length=30)

    def __str__(self):
        return '%s-%s-%s-%s-%s'%(self.id,self.title,self.price,self.market_price,self.pub)

    class Meta:
        #数据库中表的名
        db_table='book'
        #在管理器后台中表的名字
        verbose_name='图书'
        #复数变单数
        verbose_name_plural=verbose_name