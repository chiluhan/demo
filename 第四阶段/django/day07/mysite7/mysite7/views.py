import time

from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(60)
def test_cache(request):
    # 假设在视图函数中,有复杂计算或复杂查询这种耗时的操作
    # time.sleep(5)
    t1 = time.time()
    return HttpResponse('t1 is %s' % t1)


def test_mw(request):
    print('------view in')
    return HttpResponse('test mw is ok')