from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from django.utils.deconstruct import deconstructible
import os

from comicsite.utils import PathAndRename
from concept.models import Concept
from concept.sketch.models import Sketch
# Create your models here.

# The user of the comic is the same as the user of the sketch
class Comic ( models.Model ):
    sketch = models.OneToOneField(Sketch, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    deleted = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField()
    work_file = models.FileField(PathAndRename('work_files'))
    files_type = models.CharField(max_length=50)

class Strip ( models.Model ):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    image = models.ImageField(PathAndRename('strips'))
    position = models.IntegerField();
