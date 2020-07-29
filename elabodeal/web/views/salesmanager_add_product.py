import uuid

from django.conf import settings
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

from elabodeal.web.views.base import BaseView
from elabodeal.web.forms.add_product import AddProductForm
from elabodeal.models import Product, Category, File, AgeCategory


class SalesManagerAddProductView(BaseView):
	auth_required = True
	seller_required = True

	def get_form(self, request = None):
		data, files = (request.POST, request.FILES) if request else (None, None)
		return AddProductForm(data, files)

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

			product = Product(
				title=form.cleaned_data['title'],
				description=form.cleaned_data['description'],
				category=category,
				user=request.user,
				author=form.cleaned_data['author'],
				price=form.cleaned_data['price'],
				page_count=form.cleaned_data['page_count'],
				isbn=form.cleaned_data['isbn']
			)
			product.save()

			for k, v in form.cleaned_data.items():
				if k.startswith('age') and v:
					if k.endswith('0'):
						product.set_age(3)
					if k.endswith('1'):
						product.set_age(7)
					if k.endswith('2'):
						product.set_age(12)
					if k.endswith('3'):
						product.set_age(16)
					if k.endswith('4'):
						product.set_age(18)
				if (k.startswith('file') or k.endswith('file')) and v:
					if k == 'file_image_0':
						product.set_cover_img(v)
					if k == 'pdf_file':			
						product.set_pdf(v)
					if k == 'mobi_file':			
						product.set_mobi(v)
					if k == 'epub_file':			
						product.set_epub(v)

			return redirect('web:salesmanager')

		categories = Category.objects.all()

		context = {
			'form': form,
			'categories': categories
		}
		return self.respond('salesmanager/add_product.html', request, context)