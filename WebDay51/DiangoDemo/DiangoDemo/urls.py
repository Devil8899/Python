"""DiangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

#将url映射到视图函数
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('news',views.shownews),
    path('Useradd',views.Useradd)
]
'''
URL配置(URLconf)就像Django 所支撑网站的目录。
它的本质是URL模式以及要为该URL模式调用的视图函数之间的映射表；
你就是以这种方式告诉Django，对于这个URL调用这段代码，对于那个URL调用那段代码。
urlpatterns = [
    url(正则表达式, views视图函数，参数，别名),
]
'''