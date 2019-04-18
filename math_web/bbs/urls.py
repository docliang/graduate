from django.conf.urls import url
from . import views
urlpatterns = [
    #显示数学建模模块的所有帖子
    url(r'^mathmodel$',views.mathmodel,name='mathmodel'),
    #显示考研数学模块的所有帖子
    url(r'^kaoyanmath$', views.kaoyanmath, name='kaoyanmath'),
    #显示数据结构与算法模块的所有帖子
    url(r'^datastruct$',views.datastruct,name='datastruct'),

    # 显示数学建模内帖子的内容
    url(r'^mathmodel/(?P<topic_id>\d+)/$', views.mm_detail, name='mm_detail'),
    # 显示考研数学内帖子的内容
    url(r'^kaoyanmath/(?P<topic_id>\d+)/$',views.ky_detail,name='ky_detail'),
    # 显示数据结构内帖子的内容
    url(r'^datastruct/(?P<topic_id>\d+)/$',views.ds_detail,name='ds_detail'),
    #发新帖
    url(r'^publish_mm/$',views.publish_mm,name='publish_mm'),
    url(r'^publish_kaoyan/$', views.publish_kaoyan, name='publish_kaoyan'),
    url(r'^publish_ds/$', views.publish_ds, name='publish_ds'),

    #保存新帖
    url(r'^sub_mm/$',views.sub_mm,name='sub_mm'),
    url(r'^sub_kaoyan/$',views.sub_kaoyan,name='sub_kaoyan'),
    url(r'^sub_ds/$',views.sub_ds,name='sub_ds'),

    #添加新的评论
    url(r'^add_comment/$',views.add_comment,name='add_comment'),

    #添加评论测试版本
    url(r'^add_comment_test/$',views.add_comment_test,name='add_comment_test'),

    url(r'^commit/$',views.commit,name='commit'),

]