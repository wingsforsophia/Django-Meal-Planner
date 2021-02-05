from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plan


# Create your views here.
def home(request):
  return render(request, 'base.html')

def plans_index(request):
  plans = Plan.objects.all()
  return render(request, 'plans/index.html', { 'plans': plans })

def plans_detail(request, plan_id):
  plan = Plan.objects.get(id=plan_id)
  return render(request, 'plans/detail.html', { 'plan': plan })

class PlanCreate(CreateView):
  model = Plan
  fields = '__all__'

class PlanUpdate(UpdateView):
  model = Plan
  fields = '__all__'

class PlanDelete(DeleteView):
  model = Plan
  success_url = '/plans/'    