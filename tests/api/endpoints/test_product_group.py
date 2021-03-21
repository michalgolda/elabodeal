from tests import APITestCase
from django.shortcuts import reverse
from elabodeal.models import User, Publisher, ProductGroup


class MeProductsGroupsEndpointTest(APITestCase):

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

	def test_get_product_groups_list(self):
		product_group = ProductGroup(
			publisher=self.publisher,
			name='test'
		)
		product_group.save()

		response = self.client.get(reverse('api:me-products-groups'))
		response_data = response.json()

		self.assertEqual(len(response_data), 1)
		self.assertEqual(response.status_code, 200)

	def test_get_product_groups_list_auth_required(self):
		self.client.logout()

		response = self.client.get(reverse('api:me-products-groups'))

		self.assertEqual(response.status_code, 401)

	def test_get_product_groups_list_publisher_only_access(self):
		self.user.publisher = None
		self.user.save()

		response = self.client.get(reverse('api:me-products-groups'))

		self.assertEqual(response.status_code, 403)

	def test_create_product_group(self):
		response = self.client.post(
			reverse('api:me-products-groups'),
			data={
				'name': 'test1'
			}
		)
		response_data = response.json()

		self.assertEqual(response.status_code, 201)
		self.assertEqual(response_data['name'], 'test1')

	def test_create_product_group_auth_required(self):
		self.client.logout()

		response = self.client.post(reverse('api:me-products-groups'))

		self.assertEqual(response.status_code, 401)

	def test_create_product_group_publisher_only_access(self):
		self.user.publisher = None
		self.user.save()

		response = self.client.post(reverse('api:me-products-groups'))

		self.assertEqual(response.status_code, 403)


class MeProductsGroupsDetailsEndpointTest(APITestCase):

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

	def test_get_product_group_details(self):
		product_group = ProductGroup(
			publisher=self.publisher,
			name='test'
		)
		product_group.save()

		response = self.client.get(
			reverse(
				'api:me-product-group-details', 
				args=[product_group.id]
			)
		)
		response_data = response.json()

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response_data['name'], 'test')

	def test_get_product_group_details_if_product_group_does_not_exists(self):
		response = self.client.get(
			reverse(
				'api:me-product-group-details', 
				args=[self.user.id]
			)
		)

		self.assertEqual(response.status_code, 404)

	def test_get_product_group_details_auth_required(self):
		self.client.logout()

		response = self.client.get(
			reverse(
				'api:me-product-group-details', 
				args=[self.user.id]
			)
		)

		self.assertEqual(response.status_code, 401)

	def test_get_product_group_details_publisher_only_access(self):
		self.user.publisher = None
		self.user.save()

		response = self.client.get(
			reverse(
				'api:me-product-group-details', 
				args=[self.user.id]
			)
		)

		self.assertEqual(response.status_code, 403)

	def test_delete_product_group(self):
		product_group = ProductGroup(
			publisher=self.publisher,
			name='test'
		)
		product_group.save()

		response = self.client.delete(
			reverse(
				'api:me-product-group-details',
				args=[product_group.id]
			)
		)

		existing_product_group = ProductGroup.objects.filter(id=product_group.id).exists()

		self.assertEqual(response.status_code, 200)
		self.assertEqual(existing_product_group, False)

	def test_delete_product_group_if_product_group_does_not_exists(self):
		response = self.client.delete(
			reverse(
				'api:me-product-group-details',
				args=[self.user.id]
			)
		)

		self.assertEqual(response.status_code, 404)

	def test_delete_product_group_auth_required(self):
		self.client.logout()

		response = self.client.delete(
			reverse(
				'api:me-product-group-details',
				args=[self.user.id]
			)
		)

		self.assertEqual(response.status_code, 401)

	def test_delete_product_group_publisher_only_access(self):
		self.user.publisher = None
		self.user.save()

		response = self.client.delete(
			reverse(
				'api:me-product-group-details',
				args=[self.user.id]
			)
		)

		self.assertEqual(response.status_code, 403)
