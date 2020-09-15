from django.http import HttpResponse


def set_cookies(request):
    resp= HttpResponse('set cookies is ok')
    #设置cookies，有效期600秒
    resp.set_cookie('uname','tedu',600)
    return resp

def get_cookies(request):
    value=request.COOKIES.get('uname','no value')
    result='cookies value is %s'%value
    return HttpResponse(result)

def delete_cookies(request):
    resp=HttpResponse('delete cookies is ok')
    resp.delete_cookie('uname')
    return resp



def set_session(request):
    request.session['uuname']='tedu'
    return HttpResponse('set session is ok')

def get_session(request):
    value= request.session.get('uuname','no value')
    result='session value is %s'%value
    return HttpResponse(result)