from django.test import TransactionTestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.shortcuts import reverse

from concept.models import Concept
from concept.strip.models import Strip
import os

# Create your tests here.
class PublicAccessSystemTestCase(TransactionTestCase):
    def setUp(self):
        john = User(username='rookie', email='john@email.com', is_active=True)
        john.set_password('password101')
        john.save()
        self.concept = Concept(title='title', description='title', user=john, published=True)
        self.concept.save()
        strip = Strip(concept=self.concept, user=john, image = SimpleUploadedFile(name='strip.jpg', content=open(os.path.join(os.getcwd(), 'test.png'), 'rb').read(), content_type='image/jpeg'))
        #  self.concept.strip = Strip(.image = SimpleUploadedFile(name='strip.jpg', content=open(os.path.join(os.getcwd(), 'test.png'), 'rb').read(), content_type='image/jpeg')
        strip.save()

    def test_page_contains_directional_links_next_previous_last_first(self):
        url = reverse('public:slug', args=[self.concept.slug])
        response = self.client.get(url, follow=True)
        self.assertContains(response, 'First')
        self.assertContains(response, 'Previous')
        self.assertContains(response, 'Random')
        self.assertContains(response, 'Next')
        self.assertContains(response, 'Last')


