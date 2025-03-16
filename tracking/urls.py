from .views import DashboardView
from django.urls import path 
from . import views

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
]