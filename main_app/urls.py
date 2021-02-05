from django.urls import path
from . import views
# from plans.views import PlanList

urlpatterns = [
    path('', views.home, name='home'),
    path('plans/', views.plans_index, name='index'), 
]