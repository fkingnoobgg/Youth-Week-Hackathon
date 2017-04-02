from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class HTUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    activation_key = models.CharField(max_length=64)
    def __str__(self):
        return str(self.user)

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)

class Node(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    latitude = models.FloatField(
        validators = [MaxValueValidator(90), MinValueValidator(-90)]
    )
    longitude = models.FloatField(
        validators=[MaxValueValidator(180), MinValueValidator(-180)]
    )
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.CharField(max_length=300)
    votes_up = models.IntegerField(
        default = 0,
        validators = [MinValueValidator(0)]
    )
    votes_down = models.IntegerField(
        default = 0,
        validators = [MinValueValidator(0)]
    )
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
