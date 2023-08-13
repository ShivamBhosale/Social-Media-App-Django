from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Index(TemplateView):
    template_name = 'banterapp/index.html'
        
class Login(TemplateView):
    template_name = 'banterapp/login.html'
    
class Home(TemplateView):
    template_name = 'banterapp/home.html'