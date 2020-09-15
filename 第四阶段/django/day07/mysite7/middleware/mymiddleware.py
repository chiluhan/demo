from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法 process_response 被调用")
        return response


class VisitLimit(MiddlewareMixin):
    visit_times = {}
    def process_request(self, request):
        ip = request.META['REMOTE_ADDR']
        if not re.match('^/test', request.path_info):
            return
        times = self.visit_times.get(ip, 0)
        if times >= 5:
            return HttpResponse('No way!!!')
        self.visit_times[ip] = times + 1
        print('%s visit we %s times' % (ip, times + 1))
