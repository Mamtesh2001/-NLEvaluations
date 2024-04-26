from django.db import models

class App(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)

class User(models.Model):
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    points_earned = models.IntegerField(default=0)
    tasks_completed = models.IntegerField(default=0)
    screenshot = models.ImageField(upload_to='screenshots/', null=True, blank=True)
