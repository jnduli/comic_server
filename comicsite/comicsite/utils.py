from django.utils.deconstruct import deconstructible
import os

@deconstructible
class PathAndRename(object):
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(instance.concept.slug, ext)
        # return the whole path to the file
        return os.path.join('media', self.path, filename)
