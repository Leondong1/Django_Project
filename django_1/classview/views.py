from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View

# Create your views here.
# 类视图的使用
class DemoView(View):

    def get(self,request):
        return HttpResponse('get page')

    def post(self,request):
        return HttpResponse('get page')


# 类视图使用装饰器
# 咱先定义一个万能的装饰器
def my_decorator(func):
    def wrapper(request,*args,**kwargs):
        print('自定义装饰器被调用')
        print('请求路径 %s' % request)

        return func(request,*args,**kwargs)

    return wrapper

# 在类视图中装饰，需要使用 method_decorator【相当于置位转化】将其转化为适用于 类视图方法的装饰器
# 简单理解 method_decorator 的作用：因为传递参数上位置不统一
# 为特定的请求方法添加装饰器
# @method_decorator(my_decorator,name='get')
@method_decorator(my_decorator,name = 'dispatch')
class DemoView2(View):
    # 为get方法添加了装饰器
    # @method_decorator(my_decorator)
    def get(self,request):
        print('get方法')
        return HttpResponse('ok')

    def post(self,request):
        print('post方法')
        return HttpResponse('ok')



