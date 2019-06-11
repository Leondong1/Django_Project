# -*- coding: utf-8 -*-
'''
@Time    : 2019-06-11 20:34
@Author  : Leon
@Contact : wangdongjie1994@gmail.com
@File    : serializers.py
@Software: PyCharm
'''

from rest_framework import serializers
from  .models import BookInfo


# class BookInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         models = BookInfo
#         fields = "__all__"

class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    logo = serializers.ImageField(label='图片', required=False)


