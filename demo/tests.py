from django.core.urlresolvers import resolve, reverse
from django.test import TestCase, RequestFactory

from .models import AffiliatedSchool
from .views import IndexView


class HomePageTest(TestCase):

    """
    Test for home page
    """

    def setUp(self):
    	self.factory = RequestFactory()

    def test_home_page_returns_correct_html(self):
        request = self.factory.get(reverse('index'))
        response = IndexView.as_view()(request)
        print(response)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>PSYSC</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
