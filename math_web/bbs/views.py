#coding=utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_comments.models import Comment
from django.contrib.contenttypes.models import ContentType
import datetime
from django.core.paginator import *
# Create your views here.


def mathmodel(request,topic_id):
    '''显示数学建模版块所有的帖子标题及summary'''
    list = Article.objects.filter(section=3)
    paginator = Paginator(list, 6)
    topic_list = paginator.page(int(topic_id))
    context = {'topic_list':topic_list}
    return render(request, "bbs/mathmodel/index.html", context)

def kaoyanmath(request,topic_id):
    '''显示考研数学版块所有的帖子标题及summary'''
    # topic_list = Article.objects.filter(section=2)
    # context = {'topic_list':topic_list}
    list = Article.objects.filter(section=2)
    paginator = Paginator(list, 6)
    topic_list = paginator.page(int(topic_id))
    context = {'topic_list': topic_list}
    return render(request, "bbs/kaoyanmath/index.html", context)

def datastruct(request,topic_id):
    '''显示数据结构与算法版块所有的帖子标题及summary'''
    list = Article.objects.filter(section=4)
    paginator = Paginator(list, 6)
    topic_list = paginator.page(int(topic_id))
    context = {'topic_list':topic_list}
    return render(request, "bbs/datastruct/index.html", context)



def mm_detail(request,topic_id):
    '''显示当前帖子的内容'''
    article = Article.objects.get(id=topic_id)
    context = {'article':article,'topic_id':topic_id}
    return render(request, 'bbs/mathmodel/detail.html', context)


def ky_detail(request,topic_id):
    '''显示当前帖子的内容'''
    article = Article.objects.get(id=topic_id)
    context = { 'article':article,'topic_id':topic_id }
    return render(request, 'bbs/kaoyanmath/detail.html', context)

def ds_detail(request,topic_id):
    '''显示当前帖子的内容'''
    article = Article.objects.get(id=topic_id)
    context = {'article':article,'topic_id':topic_id}
    return render(request,'bbs/datastruct/detail.html',context)


def publish_mm(request):
    '''发布新帖子'''

    return render(request, 'bbs/mathmodel/publish_mathmodel.html')

def publish_kaoyan(request):
    '''发布新帖子'''

    return render(request, 'bbs/kaoyanmath/publish_kaoyanmath.html')

def publish_ds(request):
    '''发布新帖子'''

    return render(request, 'bbs/datastruct/publish_datastruct.html')

def sub_mm(request):
    '''保存数学建模帖子'''
    topic_id = 1
    auth = User.objects.get(username=request.user)
    section = Section.objects.get(id=3)
    Article.objects.create(
        title=request.POST.get('title'),
        summary=request.POST.get('content')[:50],
        content=request.POST.get('content'),
        auth=auth,
        section=section,
        view_count=1,
    )
    return HttpResponseRedirect(reverse('bbs:mathmodel',args=[topic_id]))

def sub_kaoyan(request):
    '''保存考研数学帖子'''
    topic_id = 1
    auth = User.objects.get(username=request.user)
    section = Section.objects.get(id=2)
    Article.objects.create(
        title = request.POST.get('title'),
        summary =request.POST.get('content')[:50],
        content = request.POST.get('content'),
        auth = auth,
        section = section,
        view_count = 1,

    )
    return HttpResponseRedirect(reverse('bbs:kaoyanmath',args=[topic_id]))


def sub_ds(request):
    '''保存数据结构帖子'''
    topic_id = 1
    auth = User.objects.get(username=request.user)
    section = Section.objects.get(id=4)
    Article.objects.create(
        title=request.POST.get('title'),
        summary=request.POST.get('content')[:50],
        content=request.POST.get('content'),
        auth=auth,
        section=section,
        view_count=1,

    )

    return HttpResponseRedirect(reverse('bbs:datastruct',args=[topic_id]))

def add_comment(request):
    '''提交评论'''
    topic_id = request.POST.get('topic_id')
    comment = request.POST.get('comment_content')
    Comment.objects.create(
        content_type_id = 12,
        object_pk = topic_id,
        site_id = 1,
        user = request.user,
        comment = comment
    )
    return HttpResponseRedirect(reverse('bbs:ky_detail',args=[topic_id]))



def add_comment_test(request,topic_id):
    ''' 添加评论测试版本'''
    comment = request.POST.get('comment_content')
    Comment.objects.create(
        content_type_id = 12,
        object_pk = topic_id,
        site_id = 1,
        user = request.user,
        comment = comment
    )

def commit(request,topic_id):
    context = {'topic_id':topic_id}
    return render(request,'bbs/add_comment.html',context)


#全文检索
def mysearch(request):
    return render(request,'bbs/mysearch.html')








