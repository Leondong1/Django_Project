# -*- coding: utf-8 -*-
'''
@Time    : 2019-06-11 10:41
@Author  : Leon
@Contact : wangdongjie1994@gmail.com
@File    : urls.py
@Software: PyCharm
'''
from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # url(r'^bookmanage/$',views.bookmanage),
    url(r'^booktest/$',views.IndexView.as_view()),
    url(r'^books/$',views.BooksAPIView.as_view()),
    url(r'^books/(?P<pk>\d+)/$',views.BookAPIView.as_view()),

]

router = DefaultRouter()
router.register(r'books',views.BookInfoViewSet)

urlpatterns += router.urls