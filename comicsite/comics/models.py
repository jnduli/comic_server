from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from concept.models import Concept
from django.utils.deconstruct import deconstructible
import os

# Create your models here.

@deconstructible
class PathAndRename(object):
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(instance.concept.slug, ext)
        # return the whole path to the file
        return os.path.join('media', self.path, filename)

path_and_rename = PathAndRename('sketches')

class Sketch ( models.Model ):
    concept = models.OneToOneField(Concept)
    image = models.ImageField(upload_to=path_and_rename)
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
