from django.test import TestCase
from django.test import TransactionTestCase
from django.contrib.auth.models import User

# Create your tests here.

class AuthTestCase(TransactionTestCase):

    def setUp(self):
        # create user
        john = User(username='rookie', email='john@email.com', is_active=True)
        john.set_password('password101')
        john.save()

    def test_login_url(self):
        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_failed(self):
        response = self.client.post('/auth/login/', {"email":"john@em.com", "password":"password101"}, follow=True)
        self.assertEqual(len(response.redirect_chain), 0)

    def test_login_user(self):
        # login created user
        response = self.client.post('/auth/login/', {"email":"john@email.com", "password":"password101"}, follow=True)
        self.assertEqual(len(response.redirect_chain), 1)

    def test_logout(self):
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/auth/logout/', follow=True)
        self.assertEqual(len(response.redirect_chain), 1)
