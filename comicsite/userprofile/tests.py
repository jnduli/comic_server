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
        response = self.client.get('/userprofile/details/{}'.format(self.user.id), follow=True)
        self.assertRedirects(response, reverse('auth:login')+'?next=' + reverse('userprofile:details', kwargs={'pk': self.user.id}),fetch_redirect_response=False)

    def test_user_details(self):
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/userprofile/details/{}'.format(self.user.id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'john OroJackson')
        self.assertContains(response, 'john@email.com')
        self.assertContains(response, 'rookie')

    def test_user_edit_page_load_fail(self):
        response = self.client.get('/userprofile/edit/{}'.format(self.user.id), follow=True)
        self.assertRedirects(response, reverse('auth:login')+'?next=' + reverse('userprofile:edit', kwargs={'pk': self.user.id}),fetch_redirect_response=False)


    def test_user_edit(self):
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/userprofile/edit/{}'.format(self.user.id), follow=True)
        self.assertEqual(response.status_code, 200)
        new_username = 'rookierandom'
        response = self.client.post('/userprofile/edit/{}'.format(self.user.id), {
                'username': new_username,
                'email': self.user.email,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name
            }, follow=True)
        self.assertTrue(User.objects.filter(username='rookierandom').exists())

