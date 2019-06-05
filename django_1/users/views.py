from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.


def index(request):
    """
    视图
    :param request: 用于接收请求request对象
    :return: 响应对象
    """
    return HttpResponse('hello world\r\nhello Leon')