# -*- coding: utf-8 -*-
'''
@Time    : 2019-06-08 16:50
@Author  : Leon
@Contact : wangdongjie1994@gmail.com
@File    : middleware.py
@Software: PyCharm
'''


# 在请求视图被处理前，中间件由上至下依次执行
# 在请求视图被处理后，中间件由下至上依次执行

def my_middleware(get_response):
    print('init 被调用')
    def middleware(request):
        print('before request 被调用')
        response = get_response(request)
        print('after response 被调用')
        return response
    return middleware

def my_middleware2(get_response):
    print('init2 被调用')
    def middleware(request):
        print('before request2 被调用')
        response = get_response(request)
        print('after response2 被调用')
        return response
    return middleware