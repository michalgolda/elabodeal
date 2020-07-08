from tests.base import WebTestCase
from django.urls import reverse


class TestIndexView(WebTestCase):
	def test_simple(self):
		response = self.client.get(reverse('web:index'))

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')

	def test_category_loading(self):
		response = self.client.get(reverse('web:index'), { 'category': 'Ekonomia' })

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')

	def test_invalid_category_name(self):
		response = self.client.get(reverse('web:index'), { 'category': 'asdas' })

		self.assertEqual(response._headers['content-type'][1], 'text/html; charset=utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')