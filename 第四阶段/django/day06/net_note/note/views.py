from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import  Note
import html

# Create your views here.

def logging_check(fn):
    def wrap(request, *args, **kwargs):
        # 首先检查session
        if 'username' not in request.session or 'uid' not in request.session:
            # 然后检查cookies
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:
                # 跳转到登录界面
                return HttpResponseRedirect('/user/login')
            else:
                # 回写session
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)
    return wrap

@logging_check
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')

        #如果前端页面没有转义,需要我们在视图中转义,以防止xss
        # title=html.escape(title)
        # content=html.escape(content)

        # 需要从session中读取用户id
        uid=request.session.get('uid')
        # 将笔记存储到数据库
        Note.objects.create(title=title,
                            content=content,
                            user_id=uid)
        #可以跳转转列表页
        return HttpResponse('添加笔记成功！')

