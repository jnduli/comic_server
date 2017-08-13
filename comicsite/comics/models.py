from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Concept ( models.Model ):
    title = models.CharField(max_length = 200)
    description = models.TextField(unique=True)
    characters_no = models.IntegerField(blank=True,null = True)
    conversation = models.TextField(blank=True,null = True)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)

class Sketch ( models.Model ):
    concept = models.ForeignKey(Concept)
    image = models.ImageField(upload_to='sketches')
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)

class Comic ( models.Model ):
    user = models.ForeignKey(User)
    sketch = models.ForeignKey(Sketch)
    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(default=timezone.now)
    work_files = models.FileField(upload_to='work_files')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = "%i-%s" %(
                    self.id, slugify(self.title)
                    )
            super(Comic, self).save(*args, **kwargs)

class Strip ( models.Model ):
    comic = models.ForeignKey(Comic)
    image = models.ImageField(upload_to='strips')
    position = models.IntegerField();
