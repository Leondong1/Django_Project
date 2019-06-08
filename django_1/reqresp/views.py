from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json


# Create your views here.

# URL 和 查询参数
def weather(request,city,year):
    print(city)
    print(year)

    return HttpResponse("OK")

def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')

# 请求体 区分表单类型 和 非表单类型
def get_body(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')

# 非表单类型得通过 request.body属性获取最原始的请求体数据（bytes类型）
def get_body_json(request):
    json_byte = request.body
    json_str = json_byte.decode()
    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])
    return  HttpResponse('OK')

# 请求头
def get_headers(request):
    print(request.META['CONTENT_TYPE'])
    print(request.META['REQUEST_METHOD'])
    print(request.META['HTTP_ACCEPT'])
    print(request.method)
    print(request.encoding)
    print(request.path)
    return HttpResponse('OK')

# 响应部分
# JsonResponse 帮咱们将数据转化为json字符串
def response(request):

    return JsonResponse([{'city':'kk','name':'leon'},{'city':'malacca','name':'jay'}],safe=False,
                        )

# 两种方式对响应的数据进行设置（均可以采用在HttpResponse对象上进行）
def demo_view(request):
    # return HttpResponse('leon',status=400)
    # response = HttpResponse()
    # response.content = 'hello,leon'
    # response.status_code =400
    # response['name'] = 'leon'
    # return response
    return HttpResponseRedirect(content='helo,leon')

# cookie 和 session 部分
# 设置cookie 和 读取cookie
def set_cookie(request):
    response = HttpResponse('ok')
    response.set_cookie('name','leon',max_age=3600)
    return response

# request.COOKIES为字典类型
def get_cookie(request):
    cookie = request.COOKIES.get('name')
    print(cookie)
    return HttpResponse('ok')
