from tests.base import BaseTestCase

from elabodeal.api.serializers import NewPaymentIntentSerializer


class TestNewPaymentIntentSerializer(BaseTestCase):
	def test_simple(self):
		serializer = NewPaymentIntentSerializer(data={
				'email': 'test@test.pl',
				'first_name': 'test',
				'last_name': 'test',
				'phone_number': '111111111'
			})

		serializer.is_valid()

		self.assertEqual(serializer.data['email'], 'test@test.pl')
		self.assertEqual(serializer.data['first_name'], 'test')
		self.assertEqual(serializer.data['last_name'], 'test')
		self.assertEqual(serializer.data['phone_number'], '111111111')