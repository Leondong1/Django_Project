from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.


def index(request):
    """
    视图
    :param request: 用于接收请求request对象
    :return: 响应对象
    """
    return HttpResponse('hello world\r\nhello Leon1111')


def login(request):
    """
    解析咱们的路由命名 与reverse反推在重定向里面的应用
    :param request:
    :return:
    """
    url = reverse('index')
    return redirect(url)