from tests.base import WebTestCase
from django.urls import reverse

from elabodeal.models import User, VerificationCode


class TestLoginView(WebTestCase):
	def test_simple(self):
		response = self.client.get(reverse('web:login'))

		self.assertIn('csrftoken', response.cookies.keys())
		self.assertEqual(
			response._headers['content-type'][1], 
			'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'auth/login.html')

	def test_invalid_email_error(self):
		response = self.client.post(
			reverse('web:login'), 
			{ 'email': 'asd', 'password': 123 })
		self.assertFormError(
			response, 
			'form', 
			'email', 
			'Podaj poprawny email')

		self.assertIn('csrftoken', response.cookies.keys())
		self.assertEqual(
			response._headers['content-type'][1], 
			'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'auth/login.html')

	def test_invalid_email_or_password_error(self):
		response = self.client.post
		(reverse('web:login'), 
		{ 'email': '123@wp.pl', 'password': 123 })
		self.assertFormError(
			response, 
			'form', 
			'email', 
			'Nieprawidłowy email lub hasło')

		self.assertIn('csrftoken', response.cookies.keys())
		self.assertEqual(
			response._headers['content-type'][1], 
			'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'auth/login.html')


class TestRegisterView(WebTestCase):
	def test_simple(self):
		response = self.client.get(reverse('web:register'))

		self.assertIn('csrftoken', response.cookies.keys())
		self.assertEqual(
			response._headers['content-type'][1], 
			'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'auth/register.html')

	def test_username_does_exist_error(self):
		User.objects.create(email='test@test.pl', username='test', password='123')

		response = self.client.post(reverse('web:register'), {
				'username': 'test',
				'email': 'test@test.pl',
				'password1': '123',
				'password2': '123'})
		self.assertFormError(
			response, 
			'form', 
			'username', 
			'Nazwa użytkownika jest zajęta')

		self.assertIn('csrftoken', response.cookies.keys())
		self.assertEqual(
			response._headers['content-type'][1], 
			'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'auth/register.html')

	def test_invalid_email_error(self):
		response = self.client.post(reverse('web:register'), {
				'username': 'test01',
				'email': '1231',
				'password1': '123',
				'password2': '123'})
		self.assertFormError(
			response, 
			'form', 'email', 'Podaj poprawny email')

		self.assertIn('csrftoken', response.cookies.keys())
		self.assertEqual(
			response._headers['content-type'][1], 
			'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'auth/register.html')

	def test_email_does_exist_error(self):
		User.objects.create(email='test@test.pl', username='test', password='123')

		response = self.client.post(reverse('web:register'), {
				'username': 'test01',
				'email': 'test@test.pl',
				'password1': '123',
				'password2': '123'})
		self.assertFormError(
			response, 
			'form', 
			'email', 
			'Email jest zajęty')

		self.assertIn('csrftoken', response.cookies.keys())
		self.assertEqual(
			response._headers['content-type'][1], 
			'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'auth/register.html')

	def test_password_does_not_match_error(self):
		response = self.client.post(reverse('web:register'), {
				'username': 'test',
				'email': 'test@test.pl',
				'password1': '1233',
				'password2': '123'})
		self.assertFormError(
			response, 
			'form', 
			'password2', 
			'Hasła nie są takie same')

		self.assertIn('csrftoken', response.cookies.keys())
		self.assertEqual(
			response._headers['content-type'][1], 
			'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'auth/register.html')

	def test_success_register_user(self):
		form_data = {
			'username': 'test123',
			'email': 'test123@test.pl',
			'password1': '123',
			'password2': '123'}
		response = self.client.post(
			reverse('web:register'), 
			form_data, 
			follow=True)

		verify_code = VerificationCode.objects.filter(email='test123@test.pl').first()
		self.assertNotEqual(verify_code, None)

		self.assertEqual(
			response._headers['content-type'][1], 
			'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'email_verification.html')