from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from concept.models import Concept
from comicsite.utils import PathAndRename
# Create your models here.

path_and_rename = PathAndRename('strip')

class Strip( models.Model ):
    concept = models.OneToOneField(Concept, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)
    image = models.ImageField(upload_to=path_and_rename)
