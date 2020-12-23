from django.db import models
from django.dispatch import receiver


class ProductManager(models.Manager):
	def create_product(self, publisher, category,
					   title, description, price,
					   author, page_count, isbn,
					   contents, age_category):

		title = title.lower()
		url_name = title.replace(' ', '_')

		product = self.model(publisher=publisher, category=category,
							 title=title, description=description,
							 price=price, author=author, 
							 page_count=page_count, isbn=isbn, 
							 contents=contents, age_category=age_category,
							 url_name=url_name)
		product.save()
		
		return product


class Product(models.Model):
	publisher = models.ForeignKey('elabodeal.Publisher', 
						   on_delete=models.CASCADE)
	
	category = models.ForeignKey('elabodeal.Category', 
						  on_delete=models.CASCADE)

	labels = models.ManyToManyField('elabodeal.ProductLabel')
	opinions = models.OneToOneField('elabodeal.ProductOpinion', 
							 on_delete=models.CASCADE, 
							 null=True)

	title = models.CharField(max_length=50)
	description = models.CharField(max_length=400)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	author = models.CharField(max_length=30)
	page_count = models.IntegerField()
	isbn = models.CharField(max_length=13)
	contents = models.CharField(max_length=200, null=True)
	age_category = models.IntegerField()
	url_name = models.CharField(max_length=100)
	average_rating = models.FloatField(default=0)
	rating_count = models.IntegerField(default=0)
	views = models.IntegerField(default=0)

	files = OneToMany()

	cover_img = models.ForeignKey('elabodeal.File',
						   on_delete=models.CASCADE,
						   related_name='cover_img',
						   blank=True,
						   null=True)

	pdf_file = models.ForeignKey('elabodeal.File',
						   on_delete=models.CASCADE,
						   related_name='pdf',
						   blank=True,
						   null=True)

	epub_file = models.ForeignKey('elabodeal.File',
						   on_delete=models.CASCADE,
						   related_name='epub',
						   blank=True,
						   null=True)

	mobi_file = models.ForeignKey('elabodeal.File',
						   on_delete=models.CASCADE,
						   related_name='mobi',
						   blank=True,
						   null=True)

	demo_file = models.ForeignKey('elabodeal.File',
						   on_delete=models.CASCADE,
						   related_name='demo',
						   blank=True,
						   null=True)

	published_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	objects = ProductManager()

	@property
	def filled_stars(self):
		return range(int(self.average_rating))

	@property
	def empty_stars(self):
		return range(int(5 - self.average_rating))


@receiver(models.signals.post_delete, sender=Product)
def delete_files(sender, instance, **kwargs):
	if instance:
		demo_file = instance.demo_file
		if demo_file:
			demo_file.delete()

		pdf_file = instance.pdf_file
		if pdf_file:
			pdf_file.delete()

		mobi_file = instance.mobi_file
		if mobi_file:
			mobi_file.delete()

		epub_file = instance.epub_file
		if epub_file:
			epub_file.delete()

		cover_img = instance.cover_img
		if cover_img:
			cover_img.delete()