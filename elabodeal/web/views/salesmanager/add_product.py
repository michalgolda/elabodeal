import uuid

from django.conf import settings
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

from elabodeal.web.views import BaseView
from elabodeal.web.forms import AddProductForm


class SalesManagerAddProductView(BaseView):
	auth_required = True
	publisher_required = True

	def get_form(self, request = None):
		data, files = (request.POST, request.FILES) if request else (None, request)
		
		return AddProductForm(data, files)

	def get(self, request):
		form = self.get_form()

		context = {'form': form}

		return self.respond(
			'salesmanager/add_product.html', 
			request, context)

	def post(self, request):
		form = self.get_form(request)

		if form.is_valid():
			user = request.user
			publisher = user.publisher

			form.save(publisher)

			return redirect('web:salesmanager')

		context = {
			'form': form
		}
		
		return self.respond(
			'salesmanager/add_product.html', 
			request, context)
		