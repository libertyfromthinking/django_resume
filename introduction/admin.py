from django.contrib import admin
from .models import *

# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']

class CoverletterAdmin(admin.ModelAdmin):
    list_display = ['question']

class TechAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Resume, ResumeAdmin)
admin.site.register(Coverletter, CoverletterAdmin)
admin.site.register(Tech, TechAdmin)
admin.site.register(Project, ProjectAdmin)