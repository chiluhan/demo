from django.contrib import admin

from .models import Book
# Register your models here.

#模型管理器类
class BookManage(admin.ModelAdmin):
    #列表显示时，显示哪些列
    list_display = ['id','title','price','market_price','pub']
    #哪些列带链接
    list_display_links = ['id','title']
    #可以通过哪些列过滤
    list_filter = ['pub']
    #通过哪些列搜索满足条件的记录
    search_fields = ['title']
    #哪些列可以直接在列表中编辑
    list_editable = ['market_price']

#将管理器类和模型类注册到站点
admin.site.register(Book,BookManage)