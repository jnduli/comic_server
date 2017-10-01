from django.test import TransactionTestCase
from django.urls import reverse

from concept.models import Concept
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from gimp.models import Gimp
# Create your tests here.

class GimpTestCase(TransactionTestCase):

    def setUp(self):
        john = User(username='rookie', email='john@email.com', is_active=True)
        john.set_password('password101')
        john.save()
        self.concept = Concept(title='title', description='title', user=john)
        self.concept.save()

    def test_gimp_create_url_fail(self):
        url = '/gimp/concept/' + str(self.concept.id) + '/add_gimp/'
        response = self.client.get(url, follow=True)
        self.assertNotEqual(response.status_code, 404)
        self.assertRedirects(response, '%s?next=%s' %(reverse('auth:login'), url))

    def test_gimp_create_url_pass(self):
        self.client.login(username='rookie', password='password101')
        url = '/gimp/concept/' + str(self.concept.id) + '/add_gimp/'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_upload_gimp(self):
        self.client.login(username='rookie', password='password101')
        test_gimp = SimpleUploadedFile("gimp.xcf", b"file_content")
        url = '/gimp/concept/' + str(self.concept.id) + '/add_gimp/'
        response = self.client.post(url, {'file_gimp' : test_gimp}, format='multipart', follow=True)
        gimp = Gimp.objects.get(concept = self.concept)
        self.assertTrue("title" in gimp.file_gimp.name)
        self.assertRedirects(response, reverse('concept:detail_concept', kwargs={'pk':self.concept.pk}))

    def upload_gimp(self):
        self.client.login(username='rookie', password='password101')
        test_gimp = SimpleUploadedFile("gimp.xcf", b"file_content")
        url = '/gimp/concept/' + str(self.concept.id) + '/add_gimp/'
        response = self.client.post(url, {'file_gimp' : test_gimp}, format='multipart', follow=True)
#
    def test_gimp_edit_url_fail(self):
        url = '/gimp/concept/' + str(self.concept.id) + '/edit_gimp/'
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, '%s?next=%s' %(reverse('auth:login'),url))
#
    def test_gimp_edit_url_pass(self):
        self.upload_gimp()
        self.client.login(username='rookie', password='password101')
        url = '/gimp/concept/' + str(self.concept.id) + '/edit_gimp/'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_update_sketch(self):
        self.upload_gimp()
        self.client.login(username='rookie', password='password101')
        test_gimp = SimpleUploadedFile("gimp.xcf", b"file_content")
        url = '/gimp/concept/' + str(self.concept.id) + '/edit_gimp/'
        response = self.client.post(url , {'file_gimp': test_gimp}, format='multipart', follow=True)
        gimp = Gimp.objects.get(concept = self.concept)
        self.assertTrue("title" in gimp.file_gimp.name)
