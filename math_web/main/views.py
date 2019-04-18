from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404,FileResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

#欢迎页面
def welcome(request):
    return render(request,'main/welcome.html')

#首页
def home(request):
    return render(request,'main/home.html')

#资料下载
def download(request):
    file = open('', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="filename"'
    return response




