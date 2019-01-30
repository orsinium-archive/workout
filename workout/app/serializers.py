from rest_framework import serializers
from . import models


class Exercise(serializers.ModelSerializer):
    class Meta:
        model = models.Exercise
        fields = ('id', 'name')


class Day(serializers.ModelSerializer):
    class Meta:
        model = models.Day
        fields = ('id', 'name', 'exercises')


class Plan(serializers.ModelSerializer):
    class Meta:
        model = models.Plan
        fields = ('id', 'name', 'days')


class User(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'plan')
