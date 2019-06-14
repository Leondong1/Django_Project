from datetime import datetime
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render

# Create your views here.
from .models import BookInfo, HeroInfo


# REST API JSON
# GET /books/ 获取所有图书信息

class IndexView(View):
    def get(self,request):
        context = {
            'city':'beijing',
            'list':[1,2,3],
            'dict':{'name':'leon'}
        }
        return render(request,'index.html',context)

class BooksAPIView(View):
    def get(self, request):
        books = BookInfo.objects.all()
        # 查询所有图书   路由：GET /books/
        # 转化
        books_list = []
        for book in books:
            books_list.append({
                "id": book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date.strftime('%Y-%m-%d'),
                'bread': book.bread,
                'bcomment': book.bcomment,
                'logo': book.logo.url if book.logo else ''
            })

        return JsonResponse(books_list, safe=False)

    def post(self, request):
        # 前后端逻辑中最为关键的莫过于咱们格式之间的转化
        # 让咱们的数据能够很好的去兼容各自的应用场景
        json_bytes = request.body
        json_str = json_bytes.decode()
        req_data = json.loads(json_str)
        # POST /books/  新增图书
        # 咱们这里省略校验参数的逻辑

        book = BookInfo.objects.create(
            btitle=req_data.get('btitle'),
            # 因为只有咱们的 datetime 有 strptime 方法 （后面的date()是将咱们的日期时间对象转化为日期对象）
            bpub_date=datetime.strptime(req_data.get('bpub_date'), '%Y-%m-%d').date()

        )

        # 转化
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date.strftime('%Y-%m-%d'),
            'bread': book.bread,
            'bcomment': book.bcomment,
            'logo': book.logo.url if book.logo else ''
        }
        return JsonResponse(book_dict, status=201)


class BookAPIView(View):
    # GET  /books/<pk>/  获取单一图书
    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        # 转化
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date.strftime('%Y-%m-%d'),
            'bread': book.bread,
            'bcomment': book.bcomment,
            'logo': book.logo.url if book.logo else ''
        }
        return JsonResponse(book_dict)

    def put(self, request, pk):
        #         PUT /books/<pk>/  更新图书
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        req_data = json.loads(json_str)

        # 省略校验参数
        book.btitle = req_data.get('btitle')
        book.bpub_date = datetime.strptime(req_data.get('bpub_date'), '%Y-%m-%d').date()
        book.save()

        # 转化
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date.strftime('%Y-%m-%d'),
            'bread': book.bread,
            'bcomment': book.bcomment,
            'logo': book.logo.url if book.logo else ''
        }
        return JsonResponse(book_dict, status=201)

    def delete(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()
        return HttpResponse(status=204)


# 使用DRF开发的接口
from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer


class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
