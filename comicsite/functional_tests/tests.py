from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest

class WriterAddComicTest ( LiveServerTestCase ):
    fixtures = ['functional_tests/users.json']

    def setUp(self):
        self.url = self.live_server_url
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_add_comic(self):
        #John accesses the login portal
        self.browser.get(self.url+'/comics/system')
        self.assertIn('Comics', self.browser.title)
        #John inputs his email john@email.com and password password
        email_box = self.browser.find_element_by_id("email")
        self.assertEquals(email_box.get_attribute('placeholder'), 'Email')
        email_box.send_keys('john@email.com')

        pass_box = self.browser.find_element_by_id('password')
        self.assertEquals(pass_box.get_attribute('placeholder'), 'Password')
        pass_box.send_keys('password101')
        pass_box.send_keys(Keys.ENTER)
        #John then sees a page with an add comic button
        add_comic = self.browser.find_element_by_id('add_comic_button')
        self.assertIn('ADD COMIC', add_comic.text)
        #He clicks the add comic button
        #John is directed to a page that has the workflow of the comic
        #John inputs the concept for the comic
        #He inputs the description and sample conversations
        #He inputs "today i dont know what to say"
        #He inputs the same in detailed description
        #He then saves the concept
        #He goes back to home
        #He sees a concepts link and clicks on it
        #He then looks for the concept he recently added
        #He finds "today i dont know what to say"
        #He clicks on it
        #He is directed to a page where he can either edit the concept or add a sketch
        #He adds a sketch
        #TODO: add adding a comic too
        self.fail('Finish the test')
        return

""" 
class WriterRegistrationTest (unittest.TestCase):

    def setUp(self):
        self.url ='http://localhost:8000/'
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_register(self):
        #writer accesses the website
        self.browser.get(self.url+'system')
        #She sees the title comics and the name register as a writer on the page
        self.assertIn('Comics', self.browser.title)
        self.fail('Finish the test')
        #Shec clicks on the register as a writer button
        #She sees a registration form and starts filling it
        #She inputes Jane Wambui as her name
        #She input janewambui@email.com as her email
        #She inputs password102 as her password
        #She inputs password102 as her confirmation password
        #She inputs jwambui as her username
        #She clicks register
        #THe page shows her that her registration was successful
        #She also sees a login form
        #She inputs her email and password and logs in
        #She is invited with a page telling her that her registration is being reviewed.

    def test_can_login_logout(self):
        #Jane is a write in the system
        #she visits the site and inputs her email address and password
        #She successfully logs in and the page tells her so
        #She then clicks the log out button.
        #THe loign page is then showm
        self.fail("Finish the test")
"""
