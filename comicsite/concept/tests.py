from django.test import TestCase
from django.test import TransactionTestCase
from django.contrib.auth.models import User

# Create your tests here.

class ConceptTestCase(TransactionTestCase):

    def setUp(self):
        # create user
        john = User(username='rookie', email='john@email.com', is_active=True)
        john.set_password('password101')
        john.save()

    def test_concept_create_url_fail(self):
        response = self.client.get('/concept/add_concept/', follow=True)
        # response redirected to login url
        self.assertEqual(len(response.redirect_chain), 1)

    def test_concept_create_pass(self):
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/concept/add_concept/', follow=True)
        self.assertEqual(len(response.redirect_chain), 0)
        self.assertEqual(response.status_code, 200)

    def test_concept_list_url_fail(self):
        response = self.client.get('/concept/list_concepts/', follow=True)
        self.assertEqual(len(response.redirect_chain), 1)

    def test_concept_list_url_pass(self):
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/concept/list_concepts/', follow=True)
        self.assertEqual(len(response.redirect_chain), 0)
        self.assertEqual(response.status_code, 200)
