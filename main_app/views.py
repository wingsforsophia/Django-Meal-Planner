from django.shortcuts import render
from .models import Plan

# Create your views here.
def home(request):
  return render(request, 'base.html')

