# -*- coding: utf-8 -*-
'''
@Time    : 2019-06-07 11:45
@Author  : Leon
@Contact : wangdongjie1994@gmail.com
@File    : urls.py
@Software: PyCharm
'''
from django.conf.urls import url

from classview.views import my_decorator
from . import views


urlpatterns = [
    # url(路径，视图[注意：这里一定是将函数作为入口])
    url(r'^demoview/$',views.DemoView.as_view()),
    # 在URL配置中装饰 （给所有的请求方法都加上了装饰器行为）
    url(r'^demo/$',my_decorator(views.DemoView2.as_view()))
]