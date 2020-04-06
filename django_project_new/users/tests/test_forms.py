from django.test import SimpleTestCase
from users.forms import UserRegisterForm


class TestForms(SimpleTestCase):

	def test_user_form_valid(self):
		form = UserRegisterForm(data = {

		'email' : 'sapirlove24@gmail.com'
			})


		print(form.data)
		self.assertTrue(form.is_valid())
	
		