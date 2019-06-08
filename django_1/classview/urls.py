# -*- coding: utf-8 -*-
'''
@Time    : 2019-06-07 11:45
@Author  : Leon
@Contact : wangdongjie1994@gmail.com
@File    : urls.py
@Software: PyCharm
'''
from django.conf.urls import url
from . import views


urlpatterns = [
    # url(路径，视图[注意：这里一定是将函数作为入口])
    url(r'^demoview/$',views.DemoView.as_view())
]