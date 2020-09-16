from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render



def test_csrf(request):
    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    elif request.method == 'POST':
        username=request.POST.get('username')
        result = '用户名是%s' % username
        return HttpResponse(result)


def test_page(request):
    # 要分页的数据
    datas=['a','b','c','d','e']
    # 创建分页对象paginator
    paginator=Paginator(datas,2)
    # 从查询字符串获取当前页码,获取不到,默认值1
    cur_page=request.GET.get('page',1)
    # 获取当前页的数据对象page
    page=paginator.page(cur_page)
    return render(request, "test_page.html", locals())