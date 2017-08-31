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
        #John then sees a page with an add concept button
        add_concept = self.browser.find_element_by_id('add_concept_button')
        self.assertIn('ADD CONCEPT', add_concept.text.upper())
        #He clicks the add comic button
        add_concept.click()
        #John is directed to a page that has the workflow of the comic
        #John inputs the concept for the comic
        header = self.browser.find_element_by_xpath("//h3[1]")
        self.assertIn('Concept', header.text)
        #He inputs the description and sample conversations
        #He inputs "today i dont know what to say"
        concept_title = self.browser.find_element_by_id('id_title')
        concept_title.send_keys("today i dont know what to say")
        #He inputs the same in detailed description
        concept_desc = self.browser.find_element_by_id('id_description')
        concept_desc.send_keys("today i dont know what to say")
        concept_chars_no = self.browser.find_element_by_id('id_characters_no')
        concept_chars_no.send_keys("2")
        #He then saves the concept
        concept_submit = self.browser.find_element_by_id("concept_submit")
        concept_submit.click()
        #He is directed back to home
        #A message showing concept added is shown
        success_message = self.browser.find_element_by_id("success")
        self.assertEquals("Concept successfully created", success_message.text)

        #He sees a concepts link and clicks on it
        list_concept = self.browser.find_element_by_id('list_concept_button')
        list_concept.click()
        #He then looks for the concept he recently added
        concept = self.browser.find_element_by_css_selector('td:nth-of-type(1)')
        #He finds "today i dont know what to say"
        self.assertEquals("today i dont know what to say", concept.text)
        # The concept should show whether it has a sketch or not
        concept_sketch = self.browser.find_element_by_css_selector('td:nth-of-type(2)')
        self.assertEquals("None", concept_sketch.text)
        # The concept should show whether it has a comic or not
        concept_comic = self.browser.find_element_by_css_selector('td:nth-of-type(3)')
        self.assertEquals("None", concept_comic.text)
        # The concept should show whether the comic is published or not
        concept_comic_pub = self.browser.find_element_by_css_selector("td:nth-of-type(4)")
        self.assertEquals("unpublished",concept_comic_pub.text)
        #He clicks on it
        concept_details = self.browser.find_element_by_css_selector('td:nth-of-type(5) a')
        self.assertEquals('details', concept_details.text)
        concept_details.click()
        #He is directed to a page where he can either edit the concept or add a sketch
        print(self.browser.current_url)
        concept_header = self.browser.find_element_by_css_selector('header')
        self.assertEquals('today i dont know what to say', concept_header.text)
        # He sees a button written 'Add sketch'
        sketch_add_button = self.browser.find_element_by_id('sketch_add')
        self.assertEquals('Add Sketch'.upper(), sketch_add_button.text.upper())
        sketch_add_button.click()
        # He clicks on it and is directed to a form where he can add sketched
        page_header = self.browser.find_element_by_css_selector('header')
        self.assertEquals('Add Sketch', page_header.text)
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
