from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse



class DashboardView(TemplateView):
    template_name = 'tracking/dashboard.html'
    model = None
    
