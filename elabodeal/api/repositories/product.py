from elabodeal.api.repositories import Repository
from elabodeal.models import Product


class ProductRepository(Repository):
	
	def add(self, files, other_images, *args, **kwargs):
		product = Product(*args, **kwargs)
		product.save()
		
		for file in files:
			product.files.add(file)

		for other_image in other_images:
		   product.other_images.add(other_image)
		
		return product

	def get_all_by(self, *args, **kwargs):
		return Product.objects.filter(*args, **kwargs).all()

	def get_one_by(self, *args, **kwargs):
		return Product.objects.filter(*args, **kwargs).first()

	def delete_by(self, *args, **kwargs):
		return any(Product.objects.filter(*args, **kwargs).delete())