from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('plans/', views.plans_index, name='index'), 
    path('plans/<int:plan_id>/', views.plans_detail, name='detail'),
    path('plans/create/', views.PlanCreate.as_view(), name='plans_create'),
    path('plans/<int:pk>/update/', views.PlanUpdate.as_view(), name='plans_update'),
    path('plans/<int:pk>/delete/', views.PlanDelete.as_view(), name='plans_delete'),
    path('plans/<int:plan_id>/add_meal/', views.add_meal, name='add_meal'),
    path('plans/<int:pk>/meals/<int:meal_id>/delete/', views.MealDelete.as_view(), name='meal_delete'),
    path('recipes/', views.RecipeList.as_view(), name='recipes_index'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipes_detail'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    path('plans/<int:plan_id>/meals/<int:meal_id>/assoc_recipe/<int:recipe_id>/', views.assoc_recipe, name='assoc_recipe'),
]