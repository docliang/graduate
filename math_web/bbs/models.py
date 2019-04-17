from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class Section(models.Model):
    '''版块类'''
    #版块名称
    section_name = models.CharField(max_length=32,unique=True)
    def __str__(self):
        return self.section_name



class Article(models.Model):
    '''帖子内容'''
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=250,blank=True)
    content = models.TextField()
    auth = models.ForeignKey(User)
    section = models.ForeignKey(Section)
    view_count = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title











