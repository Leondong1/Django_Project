# -*- coding: utf-8 -*-
'''
@Time    : 2019-06-05 06:54
@Author  : Leon
@Contact : wangdongjie1994@gmail.com
@File    : urls.py
@Software: PyCharm
'''
from django.conf.urls import url
from . import views


urlpatterns = [
    # url(路径，视图)，
    url(r'^index/$',views.index,name='index'),

]