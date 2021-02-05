from django.db import models
from datetime import date
from django.urls import reverse 
from django.contrib.auth.models import User

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"plan_id": self.id})
        