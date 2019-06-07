# -*- coding: utf-8 -*-
'''
@Time    : 2019-06-05 21:14
@Author  : Leon
@Contact : wangdongjie1994@gmail.com
@File    : urls.py
@Software: PyCharm
'''
from django.conf.urls import url
from . import views


urlpatterns = [
    #  参数的名字以 <> 指明，两种方式：位置参数和关键字参数
    url(r'^weather/([a-z]+)/(\d+)/$',views.weather),
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d+)/$',views.weather),
    url(r'^response/$',views.response)

]