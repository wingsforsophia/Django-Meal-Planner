from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import MealForm
from .models import Plan, Meal, Recipe


# Create your views here.
def home(request):
  return render(request, 'base.html')

def plans_index(request):
  plans = Plan.objects.all()
  return render(request, 'plans/index.html', { 'plans': plans })

def plans_detail(request, plan_id):
  plan = Plan.objects.get(id=plan_id)
  meal_form = MealForm()
  return render(request, 'plans/detail.html', { 'plan': plan, 'meal_form': meal_form })

def add_meal(request, plan_id):
  form = MealForm(request.POST)
  if form.is_valid():
    new_meal = form.save(commit=False)
    new_meal.plan_id = plan_id
    new_meal.save()
  return redirect('detail', plan_id=plan_id)

class PlanCreate(CreateView):
  model = Plan
  fields = '__all__'

class PlanUpdate(UpdateView):
  model = Plan
  fields = '__all__'

class PlanDelete(DeleteView):
  model = Plan
  success_url = '/plans/'    

class MealDelete(DeleteView):
  model = Meal
  success_url = '/plans/'   

class RecipeList(ListView):
  model = Recipe

class RecipeDetail(DetailView):
  model = Recipe

class RecipeCreate(CreateView):
  model = Recipe
  fields = '__all__'
  success_url = '/recipes/' 

class RecipeUpdate(UpdateView):
  model = Recipe
  fields = '__all__'

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes/'  