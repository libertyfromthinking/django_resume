from django.urls import path
from .views import *

app_name = 'intro'

urlpatterns = [
    path('',ResumeLV.as_view(),name='main'),
    path('resume/', ResumeLV.as_view(),name='resume'),
    path('coverletter/', CoverletterLV.as_view(), name='coverletter'),
    path('tech/', TechLV.as_view(), name='tech'),
    path('project/', ProjectLV.as_view(), name='project'),
    path('project/<str:slug>/', ProjectDV.as_view(), name='project_detail'),
    path('tech/<str:tech>/', Project_techLV.as_view(), name='project_tech'),
]

