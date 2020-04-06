
from django.test import SimpleTestCase
from django.urls import reverse , resolve
from homepage.views import home , about


class TestUrls(SimpleTestCase):


	def test_home_url(self):
		url = reverse('homepage-home')
		self.assertEquals(resolve(url).func , home)

	
	def test_about_url(self):
		url = reverse('homepage-about')
		self.assertEquals(resolve(url).func , about)
	
