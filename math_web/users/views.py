from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django_comments.models import Comment
from bbs.models import Article
# Create your views here.

def logout_view(request):
    '''注销用户'''
    logout(request)
    return HttpResponseRedirect(reverse('main:home'))

def register(request):
    '''注册新用户'''
    if request.method != 'POST':
        #显示空的注册表
        form = UserCreationForm()
    else:
        #处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #让用户自动登陆，再重定向到主页
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('main:home'))

    context = {'form':form}
    return render(request,'users/register.html',context)

def profile(request):
    '''显示个人中心'''
    name = request.user
    # comment = Comment.objects.get(user_id = request.user.id)
    content = Article.objects.filter(auth_id = request.user.id)
    # article_id = Article.objects.values('id').filter(auth_id = request.user.id)
    context = {'name':name,'content':content}
    return render(request,'users/profile.html',context)



