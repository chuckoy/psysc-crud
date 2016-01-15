from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory, Client

from .factories import UserFactory


class HomePageTest(TestCase):

    """
    Tests for home page
    """

    # TODO: test the following
    # GET or POST by anonymous user (should redirect to login page)
	# GET or POST by logged-in user with no profile (should raise a UserProfile.DoesNotExist exception)
	# GET by logged-in user (should show the form)
	# POST by logged-in user with blank data (should show form errors)
	# POST by logged-in user with invalid data (should show form errors)
	# POST by logged-in user with valid data (should redirect)
	# http://stackoverflow.com/questions/11885211/how-to-write-a-unit-test-for-a-django-view

    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.client = Client()

    def test_home_page_returns_correct_html(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
