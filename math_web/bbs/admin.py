from django.contrib import admin
from .models import *
# Register your models here.
class Article_admin(admin.ModelAdmin):
    list_display = ('title','auth','summary','section_id')


class Section_admin(admin.ModelAdmin):
    list_display = ('section_name','id')


admin.site.register(Section,Section_admin)
admin.site.register(Article,Article_admin)
