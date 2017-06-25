from django.db import models

# Create your models here.

class strip ( models.Model):
    slug = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    alternative = models.CharField(max_length=200)
    
