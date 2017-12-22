from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from random import randint

# Create your models here.

class ConceptManager(models.Manager):
    def random(self):
        count = self.filter(published=True).count()
        if count == 0:
            return None
        else:
            random_index = randint(0, count - 1)
            return self.filter(published=True)[random_index]

    def published_articles(self, index):
        return self.filter(published=True)[index]

class Concept ( models.Model ):
    title = models.CharField(max_length = 200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(unique=True)
    characters_no = models.IntegerField(blank=True,null = True)
    conversation = models.TextField(blank=True,null = True)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    date_published = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = ConceptManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Concept, self).save(*args, **kwargs)

