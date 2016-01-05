from django.core.urlresolvers import resolve, reverse
from django.test import TestCase, RequestFactory

from .factories import UserFactory
from .models import AffiliatedSchool
from .views import IndexView


class HomePageTest(TestCase):

    """
    Test for home page
    """

    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()

    def test_home_page_returns_correct_html(self):
        request = self.factory.get(reverse('index'))
        request.user = self.user
        response = IndexView.as_view()(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>PSYSC</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
