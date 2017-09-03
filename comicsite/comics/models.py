from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
import os

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

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(instance.concept.slug, ext)
        # return the whole path to the file
        return os.path.join('media/', path, filename)
    return wrapper

class Sketch ( models.Model ):
    concept = models.OneToOneField(Concept)
    image = models.ImageField(upload_to=path_and_rename('sketches'))
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)

class Comic ( models.Model ):
    user = models.ForeignKey(User)
    sketch = models.OneToOneField(Sketch)
    published = models.BooleanField(default=False)
    deleted = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField()
    work_file = models.FileField(upload_to='work_files')
    files_type = models.CharField(max_length=50)

class Strip ( models.Model ):
    comic = models.ForeignKey(Comic)
    image = models.ImageField(upload_to='strips')
    position = models.IntegerField();
