from django.db import models
from django.utils import timezone
from django.utils.deconstruct import deconstructible

from django.contrib.auth.models import User
from concept.models import Concept
from comicsite.utils import PathAndRename

# Create your models here.

path_and_rename = PathAndRename('sketches')

class Sketch ( models.Model ):
    concept = models.OneToOneField(Concept)
    image = models.ImageField(upload_to=path_and_rename)
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)
