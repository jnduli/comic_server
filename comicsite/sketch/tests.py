from django.test import TestCase
from django.test import TransactionTestCase
from django.contrib.auth.models import User
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
        response = self.client.get('/sketch/concept/'+ str(self.concept.id) + '/add_sketch', follow=True )
        self.assertNotEqual(response.status_code, 404)
        self.assertTrue("/auth/login" in str(response.redirect_chain))

    def test_sketch_create_url_pass(self):
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/sketch/concept/'+ str(self.concept.id) + '/add_sketch', follow=True )
        self.assertEqual(len(response.redirect_chain), 1)

    def test_upload_sketch(self):
        test_image = open(os.path.join(os.getcwd(),'test.png'), "rb")
        # test_image.name = test_image.name.encode()
        response = self.client.post('/sketch/concept/'+ str(self.concept.id) + '/add_sketch', {'name': test_image}, format='multipart')
        print(response.status_code)
        print(response.content)
        # sketch = Sketch.objects.get(concept = self.concept)
        # # sketch = self.concept.sketch
        # self.assertTrue(os.path.exists(sketch.image))
        # self.assertTrue("title" in sketch.image)

    # test posting image 
