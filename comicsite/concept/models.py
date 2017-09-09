from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

class Concept ( models.Model ):
    title = models.CharField(max_length = 200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(unique=True)
    characters_no = models.IntegerField(blank=True,null = True)
    conversation = models.TextField(blank=True,null = True)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Concept, self).save(*args, **kwargs)
