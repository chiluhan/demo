from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
import hashlib


# Create your views here.
def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        # 非空检查
        if not username or not password_1:
            return HttpResponse('请输入用户名或密码')
        # 两次密码一致性检查
        if password_1 != password_2:
            return HttpResponse('两次密码不一致')
        # 检查用户名是否已经被使用
        old_user = User.objects.filter(username=username)
        if old_user:
            return HttpResponse('用户名已经存在')
        # 计算密码的Hash
        md5 = hashlib.md5()
        # 参数要求是字节串,不能是字符串
        md5.update(password_1.encode())
        # 计算得到16进制表示的字符串
        password_h = md5.hexdigest()
        # 将用户数据添加到数据库
        try:
            user = User.objects.create(username=username,
                                       password=password_h)
        except Exception as e:
            print('error is %s' % e)
            return HttpResponse('用户名已经存在')
        return HttpResponse('用户注册成功!')


def login_view(request):
    if request.method == 'GET':
        # 如果用户登录过,会将登录信息（username 和uid）保存到session中
        # session是类似于字典的结构
        if 'username' in request.session and 'uid' in request.session:
            return HttpResponse('您已经登录！')
        #如果session中没有,继续检查cookies
        username=request.COOKIES.get('username')
        uid=request.COOKIES.get('uid')
        #如果cookies中有登录状态的数据,回写session
        if username and uid:
            request.session['username']=username
            request.session['uid']=uid
            return HttpResponse('您已经登录！')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            old_user = User.objects.get(username=username)
        except Exception as e:
            print('login error is %s' % e)
            return HttpResponse('用户名或密码错误！')
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h != old_user.password:
            return HttpResponse('用户名或密码错误！')
        # 在session中记录用户的登录状态
        request.session['uid'] = old_user.id
        request.session['username'] = old_user.username
        # 如果用户选择了记住我,还要在cookies中保存用户登录状态
        resp = HttpResponseRedirect('/note/add')
        if 'remember' in request.POST:
            resp.set_cookie('uid', old_user.id, 3600 * 24 * 3)
            resp.set_cookie('username', old_user.username, 3600 * 24 * 3)
        return resp


def logout_view(request):
    #cookies and session 都清除
    if 'username' in request.session:
        del request.session['username']
    if 'username' in request.session:
        del request.session['uid']
    resp=HttpResponse('用户成功退出')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp
