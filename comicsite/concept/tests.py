from django.test import TestCase
from django.test import TransactionTestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Concept
# Create your tests here.

class ConceptTestCase(TransactionTestCase):

    def setUp(self):
        # create user
        john = User(username='rookie', email='john@email.com', is_active=True)
        john.set_password('password101')
        john.save()
        self.user = john

    def test_concept_create_url_fail(self):
        response = self.client.get('/concept/add_concept/', follow=True)
        self.assertRedirects(response, reverse('auth:login')+'?next=' + reverse('concept:add_concept'))

    def test_concept_create_pass(self):
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/concept/add_concept/', follow=True)
        self.assertEqual(len(response.redirect_chain), 0)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/concept/add_concept/', {
            'title':'test create pass',
            'description': 'how to test a passing test',
            'characters_no': 2,
            })
        # returns 302 because it is redirected to another page
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Concept.objects.filter(title='test create pass').exists(), True)

    def test_concept_list_url_fail(self):
        response = self.client.get('/concept/list_concepts/', follow=True)
        self.assertEqual(len(response.redirect_chain), 1)

    def test_concept_list_url_pass(self):
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/concept/list_concepts/', follow=True)
        self.assertEqual(len(response.redirect_chain), 0)
        self.assertEqual(response.status_code, 200)
    def setUp(self):
        # create user
        john = User(username='rookie', email='john@email.com', is_active=True)
        john.set_password('password101')
        john.save()
        self.user = john

    def concept_create(self):
        con = Concept(title='test edit concept', description='this is a test concept',
                characters_no = 2)
        con.user = self.user
        con.save()
        return con.id

    def test_concept_edit_url_fail(self):
        id = self.concept_create()
        response = self.client.get('/concept/edit_concept/' + str(id), follow=True)
        self.assertEqual(len(response.redirect_chain), 2)

    def test_concept_edit_url_pass(self):
        id = self.concept_create()
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/concept/edit_concept/'+ str(id), follow=True)
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(response.status_code, 200)

    def test_concept_edit(self):
        id = self.concept_create()
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/concept/edit_concept/' + str(id), follow=True)
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(response.status_code, 200)
        new_title = 'successfully edited concept'
        response = self.client.post('/concept/edit_concept/' + str(id) + '/', {
            'title': new_title,
            'description': 'how to test a passing test',
            'characters_no': 2,
            'conversation': 'random conversation'
            }, follow=True)
        self.assertTrue(Concept.objects.filter(title=new_title).exists())

    def create_concepts(self):
        random = User(username='random', email='random@email.com', is_active=True)
        random.save()
        con1 = Concept(title='test another users concept', description='this is a test concept from random user',
                characters_no = 2)
        con1.user = random; 
        con1.save()
        con = Concept(title='test edit concept', description='this is a test concept',
                characters_no = 2, published=True)
        con.user = self.user
        con.save()
        con = Concept(title='another edit concept', description='zen of is a test concept',
                characters_no = 2)
        con.user = self.user
        con.save()
        con = Concept(title='zen of edit concept', description='another this is a test concept',
                characters_no = 2, published=True)
        con.user = self.user
        con.save()

    def test_show_my_concepts_only(self):
        self.create_concepts()
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/concept/list_concepts/', follow=True)
        self.assertEqual(response.status_code, 200)
        No_concepts = len(response.context['object_list'])
        self.assertEqual(No_concepts, 3);

    def test_concept_list(self):
        self.create_concepts()
        self.client.login(username='rookie', password='password101')
        response = self.client.get('/concept/list_concepts/', follow=True)
        self.assertEqual(response.status_code, 200)
        firstConcept = response.context['object_list'][0]
        secondConcept = response.context['object_list'][1]
        self.assertEqual(firstConcept.title, 'zen of edit concept')
        
        response = self.client.get('/concept/list_concepts/', {'orderby':'date_created'})
        firstConcept = response.context['object_list'][0]
        self.assertEqual(firstConcept.title, 'test edit concept')

        response = self.client.get('/concept/list_concepts/', {'filter' : 'False'})
        firstConcept = response.context['object_list'][0]
        self.assertEqual(firstConcept.title, 'another edit concept')
        
        
        #  print(firstConcept.title, firstConcept.date_created)
        #  print(secondConcept.title, secondConcept.date_created)
        # TODO test ordering by date_created
        # TODO test ordering by title
        # TODO test ordereing by published

        #  // create 3 concepts
        #  // test if they'll be ordered accoring to date
