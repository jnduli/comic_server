from django.test import TransactionTestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.shortcuts import reverse

from concept.models import Concept
from concept.strip.models import Strip
import os


class PublicAccessSystemTestCase(TransactionTestCase):
    def setUp(self):
        john = User(username='rookie', email='john@email.com', is_active=True)
        john.set_password('password101')
        john.save()
        self.concept = Concept(
                title='title',
                description='title',
                user=john,
                published=True)
        self.concept.save()

        strip_image_path = os.path.join(os.getcwd(), 'test.png')
        strip_image = SimpleUploadedFile(
                name='strip.jpg',
                content=open(strip_image_path, 'rb').read(),
                content_type='image/jpeg')
        strip = Strip(concept=self.concept, user=john, image=strip_image)
        strip.save()

    def test_page_contains_directional_links_next_previous_last_first(self):
        url = reverse('public:slug', args=[self.concept.slug])
        response = self.client.get(url, follow=True)
        html_text = response.content.decode('utf-8').lower()
        self.assertTrue('first' in html_text)
        self.assertTrue('previous' in html_text)
        self.assertTrue('random' in html_text)
        self.assertTrue('next' in html_text)
        self.assertTrue('last' in html_text)
