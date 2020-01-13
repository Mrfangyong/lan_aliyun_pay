"""lan_aliyun_pay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', views.index),
    url('result/', views.pay_result),  # 支付宝处理完成后回调的get请求路由
    url('update_order/', views.update_order), # 支付宝处理完成后回调的post请求路由
    url('pay/', views.pay),
]