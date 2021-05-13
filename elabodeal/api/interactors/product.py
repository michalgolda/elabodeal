from elabodeal.api.interactors import Interactor
from elabodeal.api.exceptions import ResourceDoesNotExists


class BaseProductInteractor(Interactor):

	def __init__(self, product_repo):
		self.product_repo = product_repo


class GetProductListInteractor(BaseProductInteractor):

	def execute(self, publisher):
		return self.product_repo.get_all_by(publisher=publisher)


class GetProductInteractor(BaseProductInteractor):

	def execute(self, publisher, product_id):
		return self.product_repo.get_one_by(
			publisher=publisher,
			id=product_id
		)


class CreateProductInteractor(BaseProductInteractor):

	def __init__(
		self, product_group_repo, category_repo, 
		file_repo, product_language_repo, product_premiere_repo,
		*args, **kwargs
	):
		super().__init__(*args, **kwargs)

		self.file_repo = file_repo
		self.category_repo = category_repo
		self.product_group_repo = product_group_repo
		self.product_language_repo = product_language_repo
		self.product_premiere_repo = product_premiere_repo

	def execute(
		self, publisher, product_group_id,
		category_id, product_language_id, 
		title, description, contents, 
		author, isbn, price, age_category, 
		cover_img, other_images, files,
		premiere_date
	):
		if product_group_id:
			existing_product_group = self.product_group_repo.get_one_by(
				id=product_group_id
			)
			if not existing_product_group:
				raise ResourceDoesNotExists(
					'The product group with this id does not exists.'
				)
		else:
			created_product_group = self.product_group_repo.add(
				publisher=publisher
			)

			existing_product_group = created_product_group

		existing_category = self.category_repo.get_one_by(id=category_id)
		if not existing_category:
			raise ResourceDoesNotExists(
				'The category with this id does not exists.'
			)

		existing_product_language = self.product_language_repo.get_one_by(
			id=product_language_id
		)
		if not existing_product_language:
			raise ResourceDoesNotExists(
				'The product language with this id does not exists.'
			)

		uploaded_cover_img = self.file_repo.add(cover_img, type='cover')
		uploaded_other_images = [
			self.file_repo.add(other_image, type='image') for other_image in other_images
		]
		uploaded_files = [
			self.file_repo.add(file, type='ebook') for file in files
		]

		premiere = self.product_premiere_repo.add(date=premiere_date) if premiere_date else None

		return self.product_repo.add(
			publisher=publisher,
			group=existing_product_group,
			category=existing_category,
			language=existing_product_language,
			age_category=age_category,
			title=title,
			description=description,
			contents=contents,
			author=author,
			isbn=isbn,
			price=price,
			cover_img=uploaded_cover_img,
			files=uploaded_files,
			other_images=uploaded_other_images,
			premiere=premiere
		)


class DeleteProductInteractor(BaseProductInteractor):

	def execute(self, publisher, product_id):
		return self.product_repo.delete_by(
			publisher=publisher,
			id=product_id
		)