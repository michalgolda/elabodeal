import json

from django.core.serializers import serialize

from elabodeal.web.views import BaseView
from elabodeal.models import ProductLanguage, Category


class SalesManagerAddProductView(BaseView):
	auth_required = True
	publisher_required = True

	def _getSupportedLanguages(self):
		product_languages_queryset = ProductLanguage.objects.all()

		supported_languages = []
		for product_language in product_languages_queryset:
			product_language_id = str(product_language.id)
			product_language_name = product_language.name
			product_language_code = product_language.code

			supported_languages.append(
				dict(
					id=product_language_id,
					name=product_language_name,
					code=product_language_code
				)
			)

		return supported_languages

	def _getCategories(self):
		categories_queryset = Category.objects.all()
		categories = []

		for category in categories_queryset:
			category_id = str(category.id)
			category_name = str(category.name)

			categories.append(
				dict(
					id=category_id,
					name=category_name
				)
			)

		return categories

	def _getFee(self):
		return 1.25

	def _getContextData(self):
		return json.dumps(
			dict(
				categories=self._getCategories(),
				supportedLanguages=self._getSupportedLanguages(),
				fee=self._getFee()
			)
		)

	def get(self, request):
		context = {}
		context['data'] = self._getContextData()

		return self.respond('salesmanager/add_product.html', request, context)