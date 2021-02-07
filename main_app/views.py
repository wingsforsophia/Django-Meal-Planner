from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import MealForm
from .models import Plan, Meal, Recipe, Photo
import uuid
import boto3
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'djangomealplanner'

# Create your views here.
def home(request):
  return render(request, 'base.html')

def plans_index(request):
  plans = Plan.objects.all()
  return render(request, 'plans/index.html', { 'plans': plans })

def plans_detail(request, plan_id):
  plan = Plan.objects.get(id=plan_id)
  recipes = Recipe.objects.all()
  meal_form = MealForm()
  return render(request, 'plans/detail.html', { 'plan': plan, 'recipes': recipes, 'meal_form': meal_form })

def add_meal(request, plan_id):
  form = MealForm(request.POST)
  if form.is_valid():
    new_meal = form.save(commit=False)
    new_meal.plan_id = plan_id
    new_meal.save()
  return redirect('detail', plan_id=plan_id)

def assoc_recipe(request, plan_id, meal_id, recipe_id):
  Plan.objects.get(id=plan_id).Meal.objects.get(id=meal_id).recipe.add(recipe_id)
  return redirect('detail', plan_id=plan_id)  

def add_photo(request, recipe_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, recipe_id=recipe_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', recipe_id=recipe_id)


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