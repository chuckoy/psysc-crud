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
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>PSYSC Database</title>', response.content)
