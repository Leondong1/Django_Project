from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
# 类视图的使用
class DemoView(View):

    def get(self,request):
        return HttpResponse('get page')

    def post(self,request):
        return HttpResponse('get page')

        e