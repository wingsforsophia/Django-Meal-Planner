from django.contrib import admin
from .models import Plan, Meal, Recipe, Photo

# Register your models here.

admin.site.register(Plan)
admin.site.register(Meal)
admin.site.register(Recipe)
admin.site.register(Photo)
