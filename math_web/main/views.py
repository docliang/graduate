from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

#首页
def home(request):
    return render(request,'main/home.html')