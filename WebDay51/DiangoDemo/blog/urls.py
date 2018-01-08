#_author: liuz
#date: 2018/1/8

from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from blog import views
#单个应用的分发 拿car/bmw举例  访问路径就是 http://127.0.0.1:8000/blog/car/bmw
urlpatterns = [
    url('car/bmw',views.bmw),
    url('login',views.login2,name='ind')
]