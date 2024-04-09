from django.db import models

# Create your models here.
class Person(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

