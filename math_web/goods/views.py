from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    '''主页，显示所有图书'''
    return render(request,'goods/index.html')

