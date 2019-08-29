from django.contrib import admin
from .models import *

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}

class PhotoAdmin(admin.ModelAdmin):
    list_diplay = ['title', 'upload_date']

admin.site.register(Board, BoardAdmin)
admin.site.register(Comment)