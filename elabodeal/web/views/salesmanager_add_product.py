import uuid

from django.conf import settings
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

from elabodeal.web.views.base import BaseView
from elabodeal.web.forms.add_product import AddProductForm
from elabodeal.models import Product, Category, File


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

			fs_static = FileSystemStorage(location=f'{settings.BASE_DIR}/elabodeal/web/static/cover_images/')
			fs_media = FileSystemStorage()

			cover_img = None
			pdf = None
			epub = None
			mobi = None

			for k, v in form.cleaned_data.items():
				if (k.startswith('file') or k.endswith('file')) and v:
					file = v
					file_size = file.size
					file_name = uuid.uuid4()
					file_content_type = file.content_type

					if k == 'file_image_0':
						file_extenstion = file_content_type.split('image/')[1]
						file_url = f'/static/cover_images/{file_name}.{file_extenstion}'

						fs_static.save(f'{file_name}.{file_extenstion}', file)

						cover_img = File(
							name=file_name,
							extension=file_extenstion,
							mime=file_content_type,
							size=file_size,
							url=file_url
						)

						cover_img.save()

					file_extenstion = file_content_type[-3:]
					file_url = f'/api/files/{file_name}.{file_extenstion}/'

					if k == 'pdf_file':			
						fs_media.save(f'{file_name}.{file_extenstion}', file)

						pdf = File(
							name=file_name,
							extension=file_extenstion,
							mime=file_content_type,
							size=file_size,
							url=file_url
						)
						pdf.save()

					if k == 'mobi_file':			
						fs_media.save(f'{file_name}.{file_extenstion}', file)

						mobi = File(
							name=file_name,
							extension=file_extenstion,
							mime=file_content_type,
							size=file_size,
							url=file_url
						)
						mobi.save()

					if k == 'epub_file':			
						fs_media.save(f'{file_name}.{file_extenstion}', file)

						epub = File(
							name=file_name,
							extension=file_extenstion,
							mime=file_content_type,
							size=file_size,
							url=file_url
						)
						epub.save()

			product = Product(
				title=form.cleaned_data['title'],
				description=form.cleaned_data['description'],
				category=category,
				user=request.user,
				author=form.cleaned_data['author'],
				price=form.cleaned_data['price'],
				page_count=form.cleaned_data['page_count'],
				isbn=form.cleaned_data['isbn'],
				cover_img=cover_img,
				pdf=pdf,
				mobi=mobi,
				epub=epub
			)
			product.save()

			return redirect('web:salesmanager')

		categories = Category.objects.all()

		context = {
			'form': form,
			'categories': categories
		}
		return self.respond('salesmanager/add_product.html', request, context)