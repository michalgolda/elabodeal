from io import BytesIO
from unittest import mock
from copy import deepcopy
from shutil import rmtree
from tempfile import mkdtemp

from PIL import Image

from tests import APITestCase

from django.core.files import File
from django.shortcuts import reverse
from django.test import override_settings

from elabodeal.models import (
	User, Publisher, Product, 
	ProductGroup, ProductLanguage,
	Category
)


TEMPORARY_MEDIA_ROOT = mkdtemp()


class MeProductsEndpointTest(APITestCase):

	def setUp(self):
		self.user = User.objects.create_user(
			email='xyz@xyz.pl',
			username='xyz',
			password='xyz'
		)

		self.publisher = Publisher.objects.create_publisher(
			first_name='test',
			last_name='test',
			swift='123',
			account_number='123'
		)

		self.user.publisher = self.publisher
		self.user.save()

		self.client.login(
			email='xyz@xyz.pl',
			password='xyz'
		)

	def test_get_products_list(self):
		response = self.client.get(reverse('api:me-products'))
		response_data = response.json()

		self.assertEqual(type(response_data), list)
		self.assertEqual(response.status_code, 200)

	def test_get_products_list_auth_required(self):
		self.client.logout()

		response = self.client.get(reverse('api:me-products'))

		self.assertEqual(response.status_code, 401)

	def test_get_products_list_publisher_only_access(self):
		self.user.publisher = None
		self.user.save()

		response = self.client.get(reverse('api:me-products'))

		self.assertEqual(response.status_code, 403)

	@override_settings(MEDIA_ROOT=TEMPORARY_MEDIA_ROOT)
	def test_create_product(self):
		product_language = ProductLanguage.objects.create(
			name='english',
			code='EN'
		)
		category = Category.objects.create(
			name='test'
		)

		ebook_file_io = BytesIO(b'ajwdawjdaw')
		image_file_io = BytesIO()

		pillow_image = Image.new('RGB', size=(100, 100), color='white')
		pillow_image.save(image_file_io, format='jpeg')
		
		image_file_io.seek(0)
		
		cover_img = File(
			deepcopy(image_file_io), 
			name='test.jpg'
		)
		ebook_file = File(
			deepcopy(ebook_file_io), 
			name='test.epub'
		)
		other_image_file = File(
			deepcopy(image_file_io), 
			name='test.png'
		)
	
		response = self.client.post(
			reverse('api:me-products'),
			data={
				'product_language_id': str(product_language.id),
				'category_id': str(category.id),
				'title': 'testtesttest',
				'description': 'test',
				'contents': 'test',
				'author': 'test',
				'isbn': '1231231231231',
				'price': 12.00,
				'age_category': 7,
				'cover_img': cover_img,
				'files': [ebook_file],
				'other_images': [other_image_file]
			}
		)
		response_data = response.json()

		self.assertEqual(response.status_code, 201)

	@override_settings(MEDIA_ROOT=TEMPORARY_MEDIA_ROOT)
	def test_create_product_with_product_group_id(self):
		product_group = ProductGroup.objects.create(
			publisher=self.publisher
		)
		product_language = ProductLanguage.objects.create(
			name='english',
			code='EN'
		)
		category = Category.objects.create(
			name='test'
		)

		ebook_file_io = BytesIO(b'ajwdawjdaw')
		image_file_io = BytesIO()

		pillow_image = Image.new('RGB', size=(100, 100), color='white')
		pillow_image.save(image_file_io, format='jpeg')
		
		image_file_io.seek(0)
		
		cover_img = File(
			deepcopy(image_file_io), 
			name='test.jpg'
		)
		ebook_file = File(
			deepcopy(ebook_file_io), 
			name='test.epub'
		)
		other_image_file = File(
			deepcopy(image_file_io), 
			name='test.png'
		)
	
		response = self.client.post(
			reverse('api:me-products'),
			data={
				'product_group_id': str(product_group.id),
				'product_language_id': str(product_language.id),
				'category_id': str(category.id),
				'title': 'testtesttest',
				'description': 'test',
				'contents': 'test',
				'author': 'test',
				'isbn': '1231231231231',
				'price': 12.00,
				'age_category': 7,
				'cover_img': cover_img,
				'files': [ebook_file],
				'other_images': [other_image_file]
			}
		)
		response_data = response.json()

		self.assertEqual(response.status_code, 201)


	def test_create_product_auth_required(self):
		self.client.logout()

		response = self.client.post(reverse('api:me-products'))

		self.assertEqual(response.status_code, 401)

	def test_create_product_publisher_only_access(self):
		self.user.publisher = None
		self.user.save()

		response = self.client.post(reverse('api:me-products'))

		self.assertEqual(response.status_code, 403)

	def tearDown(self):
		rmtree(TEMPORARY_MEDIA_ROOT, ignore_errors=True)


class MeProductsDetailsEndpointTest(APITestCase):

	def setUp(self):
		self.user = User.objects.create_user(
			email='xyz@xyz.pl',
			username='xyz',
			password='xyz'
		)

		self.publisher = Publisher.objects.create_publisher(
			first_name='test',
			last_name='test',
			swift='123',
			account_number='123'
		)

		self.user.publisher = self.publisher
		self.user.save()

		self.client.login(
			email='xyz@xyz.pl',
			password='xyz'
		)

	def test_get_product_details_auth_required(self):
		self.client.logout()

		response = self.client.get(
			reverse(
				'api:me-product-details', 
				args=[self.user.id]
			)
		)

		self.assertEqual(response.status_code, 401)

	def test_get_product_details_publisher_only_access(self):
		self.user.publisher = None
		self.user.save()

		response = self.client.get(
			reverse(
				'api:me-product-details',
				args=[self.user.id]
			),
		)

		self.assertEqual(response.status_code, 403)

	# def test_delete_product(self):

	def test_delete_product_auth_required(self):
		self.client.logout()

		response = self.client.delete(
			reverse(
				'api:me-product-details', 
				args=[self.user.id]
			)
		)

		self.assertEqual(response.status_code, 401)

	def test_delete_product_publisher_only_access(self):
		self.user.publisher = None
		self.user.save()

		response = self.client.delete(
			reverse(
				'api:me-product-details',
				args=[self.user.id]
			),
		)

		self.assertEqual(response.status_code, 403)
