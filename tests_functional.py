import unittest

from selenium import webdriver


class ServerIsRunningTest(unittest.TestCase):

    """
    Test to check if the server can be accessed via Firefox
    """

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def runTest(self):
        # Access the site
        self.browser.get('http://localhost:8000/demo')

        # Check the title of the site; did I go to the right page?
        self.assertIn('PSYSC', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
