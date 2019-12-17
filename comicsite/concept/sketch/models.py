from django.db import models
from django.utils import timezone
from concept.models import Concept
from comicsite.utils import PathAndRename

path_and_rename = PathAndRename('sketches')


# The user of the sketch is the same as the user of the concept
class Sketch (models.Model):
    concept = models.OneToOneField(Concept, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=path_and_rename)
    date_created = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)
