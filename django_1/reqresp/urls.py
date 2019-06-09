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
    url(r'^qs/$',views.qs),
    url(r'^getbody/$',views.get_body),
    url(r'^getjson/$',views.get_body_json),
    url(r'^getheaders/$',views.get_headers),
    url(r'^response/$',views.response),
    url(r'^demoview/$', views.demo_view),
    url(r'^setcookie/$',views.set_cookie),
    url(r'^getcookie/$',views.get_cookie),
    url(r'^setsession/$',views.set_session),
    url(r'^setsession2/$',views.set_session)


]