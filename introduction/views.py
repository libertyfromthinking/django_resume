from django.shortcuts import render
from .models import *
from django.views.generic import ListView, TemplateView, DetailView

# Create your views here.
class ResumeLV(ListView):
    model = Resume
    
class CoverletterLV(ListView):
    model = Coverletter

class TechLV(ListView):
    model = Tech

class ProjectLV(ListView):
    model = Project

class Project_techLV(ListView):
    template_name = 'introduction/tech_project_list.html'
    model = Project
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tech = self.kwargs['tech']
        tech_name=Tech.objects.get(name=tech)
        context['tech'] =  tech
        context['object_list'] = Project.objects.filter(techs__in=[tech_name])
        return context
            
class ProjectDV(DetailView):
    model = Project