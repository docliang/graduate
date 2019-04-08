#主页url配置
from django.conf.urls import url
from . import views

urlpatterns =[

    url(r'^$',views.home,name='home'),
]