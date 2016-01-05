from unittest import TestCase

from selenium import webdriver


class ServerIsRunningTest(TestCase):

    def runTest(self):
        browser = webdriver.Firefox()
        browser.get('http://localhost:8000')
        assert 'Django' in browser.title
