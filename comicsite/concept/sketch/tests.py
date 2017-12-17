from django.test import TestCase
from django.test import TransactionTestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from concept.models import Concept
from .models import Sketch
import os

# Create your tests here.

class SketchTestCase(TransactionTestCase):

    def setUp(self):
        # create user
        john = User(username='rookie', email='john@email.com', is_active=True)
        john.set_password('password101')
        john.save()
        concept = Concept(title='title',description='title',user=john)
        concept.save()
        self.concept = concept


    def test_sketch_create_url_fail(self):
        url = '/sketch/concept/'+ str(self.concept.id) + '/add_sketch/'
        response = self.client.get(url, follow=True )
        self.assertNotEqual(response.status_code, 404)
        self.assertRedirects(response, '%s?next=%s' %(reverse('auth:login'), url))
        #  self.assertTrue("/auth/login" in str(response.redirect_chain))

    def test_sketch_create_url_pass(self):
        self.client.login(username='rookie', password='password101')
        url = '/sketch/concept/'+ str(self.concept.id) + '/add_sketch/'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_upload_sketch(self):
        self.client.login(username='rookie', password='password101')
        test_image = open(os.path.join(os.getcwd(),'test.png'), "rb")
        # test_image.name = test_image.name.encode()
        url = '/sketch/concept/'+ str(self.concept.id) + '/add_sketch/'
        response = self.client.post(url , {'image': test_image}, format='multipart', follow=True)
        sketch = Sketch.objects.get(concept = self.concept)
        self.assertTrue("title" in sketch.image.name)
        self.assertRedirects(response, reverse('concept:detail_concept', kwargs={'pk':self.concept.pk}))

    def upload_sketch(self):
        self.client.login(username='rookie', password='password101')
        test_image = open(os.path.join(os.getcwd(),'test.png'), "rb")
        url = '/sketch/concept/'+ str(self.concept.id) + '/add_sketch/'
        response = self.client.post(url , {'image': test_image}, format='multipart', follow=True)

    def test_sketch_edit_url_fail(self):
        url = '/sketch/concept/' + str(self.concept.id) + '/edit_sketch/'
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, '%s?next=%s' %(reverse('auth:login'),url))

    def test_sketch_edit_url_pass(self):
        self.upload_sketch()
        self.client.login(username='rookie', password='password101')
        url = '/sketch/concept/' + str(self.concept.id) + '/edit_sketch/'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_update_sketch(self):
        self.upload_sketch()
        self.client.login(username='rookie', password='password101')
        test_image = open(os.path.join(os.getcwd(),'test.png'), "rb")
        # test_image.name = test_image.name.encode()
        url = '/sketch/concept/'+ str(self.concept.id) + '/edit_sketch/'
        response = self.client.post(url , {'image': test_image}, format='multipart', follow=True)
        sketch = Sketch.objects.get(concept = self.concept)
        # sketch = self.concept.sketch
        self.assertTrue("title" in sketch.image.name)
