from django.db import models
from datetime import date
from django.urls import reverse 
from django.contrib.auth.models import User

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
class Recipe(models.Model):
    name = models.CharField(max_length=100)  
    url =  models.CharField(max_length=250) 
    photo_url = models.CharField(max_length=250)
    blog_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.id})    

class Plan(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"plan_id": self.id})
        
class Meal(models.Model):
    date = models.DateField('meal date')
    name = models.CharField(max_length=100)
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[2][0]
    ) 
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE) 
    recipe = models.ManyToManyField(Recipe)     

    def __str__(self):
        return f"{self.name}, {self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['date']    