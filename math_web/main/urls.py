#主页url配置
from django.conf.urls import url
from . import views

urlpatterns =[

    url(r'^$',views.welcome,name='welcome'),
    url(r'^home/$',views.home,name='home'),
    url(r'^download/(?P<filename>\s+)/$',views.download,name='download'),
]