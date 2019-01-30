# external
from django.contrib.auth.models import AbstractUser
from django.db import models


class Exercise(models.Model):
    name = models.CharField('Name', max_length=16)


class Day(models.Model):
    name = models.CharField('Name', max_length=16)
    exercises = models.ManyToManyField(Exercise, 'Exercises')


class Plan(models.Model):
    name = models.CharField('Name', max_length=16)
    days = models.ManyToManyField(Day, 'Days')


class User(AbstractUser):
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, default=None)
