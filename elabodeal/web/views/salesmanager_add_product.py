from django.shortcuts import redirect

from elabodeal.web.views.base import BaseView
from elabodeal.web.forms.add_product import AddProductForm
from elabodeal.models import Product, Category

class SalesManagerAddProductView(BaseView):
	auth_required = True
	seller_required = True

	def get_form(self, request = None):
		return AddProductForm(request.POST if request else None)

	def get(self, request):
		categories = Category.objects.all()

		context = {
			'form': self.get_form(),
			'categories': categories
		}
		return self.respond('salesmanager/add_product.html', request, context)

	def post(self, request):
		form = self.get_form(request)

		if form.is_valid():
			category = Category.objects.filter(name=request.POST.get('category')).first()
			product = Product()
			product.category = category
			product.author = request.user
			product.title = form.cleaned_data['title']
			product.description = form.cleaned_data['description']
			product.price = form.cleaned_data['price']
			product.cover_img_url = form.cleaned_data['cover_img_url']
			product.isbn = form.cleaned_data['isbn']
			product.page_count = form.cleaned_data['page_count']

			product.save()

			return redirect('web:salesmanager')

		context = {
			'form': form
		}
		return self.respond('salesmanager/add_product.html', request, context)