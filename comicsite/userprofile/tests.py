from django.test import TransactionTestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class UserProfileTestCase(TransactionTestCase):

    def setUp(self):
        # create user
        john = User(username='rookie', email='john@email.com', first_name='john', last_name='OroJackson', is_active=True)
        john.set_password('password101')
        john.save()
        self.user = john

    def test_user_details_page_load_fail(self):
        response = self.client.get('/userprofile/details/', follow=True)
        self.assertRedirects(response, reverse('auth:login')+'?next=' + reverse('userprofile:details'))
