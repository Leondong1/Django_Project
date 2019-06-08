"""django_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin


import users.urls
from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 咱们尽量别这么使用，毕竟将来项目很多视图，会导致文件累赘
    # url(r'users/',views.index),
    # url(r'^users/',include('users.urls',namespace='users'))
    # 注意这里的两种方式均可以找到咱们的子路由
    url(r'^users/',include(users.urls)),
    url(r'reqresp/',include('reqresp.urls')),
    url(r'^classview/$',include('classview.urls'))
]
