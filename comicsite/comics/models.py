from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from django.utils.deconstruct import deconstructible
import os

from comicsite.utils import PathAndRename
from concept.models import Concept
from sketch.models import Sketch
# Create your models here.


class Comic ( models.Model ):
    user = models.ForeignKey(User)
    sketch = models.OneToOneField(Sketch)
    published = models.BooleanField(default=False)
    deleted = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField()
    work_file = models.FileField(PathAndRename('work_files'))
    files_type = models.CharField(max_length=50)

class Strip ( models.Model ):
    comic = models.ForeignKey(Comic)
    image = models.ImageField(PathAndRename('strips'))
    position = models.IntegerField();
