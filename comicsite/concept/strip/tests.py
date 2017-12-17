from django.test import TransactionTestCase
from django.urls import reverse

from concept.models import Concept
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from concept.strip.models import Strip
import os
# Create your tests here.

class StripTestCase(TransactionTestCase):

    def setUp(self):
        john = User(username='rookie', email='john@email.com', is_active=True)
        john.set_password('password101')
        john.save()
        self.concept = Concept(title='title', description='title', user=john)
        self.concept.save()

    def test_strip_create_url_fail(self):
        url = '/strip/concept/' + str(self.concept.id) + '/add_strip/'
        response = self.client.get(url, follow=True)
        self.assertNotEqual(response.status_code, 404)
        self.assertRedirects(response, '%s?next=%s' %(reverse('auth:login'), url))

    def test_strip_create_url_pass(self):
        self.client.login(username='rookie', password='password101')
        url = '/strip/concept/' + str(self.concept.id) + '/add_strip/'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_upload_strip(self):
        self.client.login(username='rookie', password='password101')
        test_strip = open(os.path.join(os.getcwd(),'test.png'), "rb")
        url = '/strip/concept/' + str(self.concept.id) + '/add_strip/'
        response = self.client.post(url, {'image' : test_strip}, format='multipart', follow=True)
        strip = Strip.objects.get(concept = self.concept)
        self.assertTrue("title" in strip.image.name)
        self.assertRedirects(response, reverse('concept:detail_concept', kwargs={'pk':self.concept.pk}))

    def upload_strip(self):
        self.client.login(username='rookie', password='password101')
        test_strip = open(os.path.join(os.getcwd(),'test.png'), "rb")
        url = '/strip/concept/' + str(self.concept.id) + '/add_strip/'
        response = self.client.post(url, {'image' : test_strip}, format='multipart', follow=True)
#
    def test_strip_edit_url_fail(self):
        url = '/strip/concept/' + str(self.concept.id) + '/edit_strip/'
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, '%s?next=%s' %(reverse('auth:login'),url))

    def test_strip_edit_url_pass(self):
        self.upload_strip()
        self.client.login(username='rookie', password='password101')
        url = '/strip/concept/' + str(self.concept.id) + '/edit_strip/'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    #  def test_update_sketch(self):
        #  self.upload_strip()
        #  self.client.login(username='rookie', password='password101')
        #  test_strip = SimpleUploadedFile("strip.xcf", b"file_content")
        #  url = '/strip/concept/' + str(self.concept.id) + '/edit_strip/'
        #  response = self.client.post(url , {'image': test_strip}, format='multipart', follow=True)
        #  strip = Strip.objects.get(concept = self.concept)
        #  self.assertTrue("title" in strip.image.name)
