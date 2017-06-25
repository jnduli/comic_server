from selenium import webdriver
import unittest

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

if __name__ == '__main__':
    unittest.main(warnings='ignore')

