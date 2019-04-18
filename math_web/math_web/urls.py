"""math_web URL Configuration

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

urlpatterns = [
    url(r'^admin/', admin.site.urls),#后台
    url(r'^',include('main.urls',namespace='main')),#主页面
    url(r'^note/',include('note.urls',namespace='note')),#笔记
    url(r'^users/',include('users.urls',namespace='users')),#用户
    url(r'^tinymce/',include('tinymce.urls')),#富文本编辑器
    url(r'^bbs/',include('bbs.urls',namespace='bbs')),#论坛
    url(r'^comments/', include('django_comments.urls',namespace='comments')),#评论
    url(r'^goods/$',include('goods.urls',namespace='goods')),#商品
    url(r'^search/',include('haystack.urls')),
]
