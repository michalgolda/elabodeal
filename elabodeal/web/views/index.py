from django.http import HttpResponse
from django.views import View
from django.template.loader import render_to_string

from elabodeal.models import Category


class IndexView(View):
	def respond_index(self, request, context = None):
		return HttpResponse(render_to_string('index.html', context, request))

	def get(self, request):
		categories = Category.objects.all()

		context = {
			'categories': categories,
			'products': [
				{
					'title': 'Test',
					'author': 'Krzystof Bosak',
					'price': 123
				},
				{
					'title': 'Test',
					'author': 'Krzystof Bosak',
					'price': 123
				},
				{
					'title': 'Test',
					'author': 'Krzystof Bosak',
					'price': 123
				}
			]
		}
		return self.respond_index(request, context)