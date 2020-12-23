from django import forms
from django.core.exceptions import ValidationError

from elabodeal.web.forms import validators
from elabodeal.models import Category, Product, File


LANG_CHOICES = [
	('PL', 'Polski'),
	('DE', 'Niemiecki'),
	('EN', 'Angielski')]


class AddProductForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(AddProductForm, self).__init__(*args, **kwargs)

		categories = Category.objects.all()

		CATEGORY_CHOICES = [(c.name, c.name) for c in categories]

		self.fields['category'] = forms.ChoiceField(
			choices=CATEGORY_CHOICES,
			widget=forms.Select)

	lang = forms.ChoiceField(
		choices=LANG_CHOICES,
		widget=forms.Select)

	contents = forms.CharField(widget=forms.Textarea)

	title = forms.CharField(widget=forms.TextInput)

	description = forms.CharField(widget=forms.Textarea)

	author = forms.CharField(widget=forms.TextInput)

	isbn = forms.CharField(widget=forms.TextInput)

	page_count = forms.IntegerField(
		widget=forms.NumberInput(
			attrs={'min': '1'}), )

	price = forms.DecimalField(
		widget=forms.NumberInput(
			attrs={'min': '1'}), )

	copies = forms.IntegerField(widget=forms.NumberInput)

	ebook_file_pdf = forms.FileField(
		required=False,
		validators=[validators.ebook_file_size],
		widget=forms.FileInput(
			attrs={
				'id': 'ebook-file-input',
				'accept': '.pdf'}))

	ebook_file_mobi = forms.FileField(
		required=False,
		validators=[validators.ebook_file_size],
		widget=forms.FileInput(
			attrs={
				'id': 'ebook-file-input',
				'accept': '.mobi'}))

	ebook_file_epub = forms.FileField(
		required=False,
		validators=[validators.ebook_file_size],
		widget=forms.FileInput(
			attrs={
				'id': 'ebook-file-input',
				'accept': '.epub'}))

	ebook_file_demo = forms.FileField(
		required=False,
		validators=[validators.ebook_file_size],
		widget=forms.FileInput(
			attrs={
				'id': 'ebook-file-input',
				'accept': '.pdf'}))

	cover_img = forms.FileField(
		required=True,
		validators=[validators.image_file_size],
		widget=forms.FileInput(
			attrs={
				'id': 'image-file-input',
				'accept': '.jpg'}))

	age_category = forms.IntegerField(widget=forms.HiddenInput)	

	accept_rules = forms.BooleanField(widget=forms.CheckboxInput)

	def clean_category(self):
		category_name = self.cleaned_data.get('category')

		category = Category.objects.filter(name=category_name).first()
		if not category:
			self.add_error(
				'category',
				'Podana kategoria nie istnieje')

		return category

	def clean_age_category(self):
		age_category = self.cleaned_data.get('age_category')

		_supported_categories = [3, 7, 12, 16, 18]

		if not age_category in _supported_categories:
			self.add_error(
				'age_cateogory',
				'Podana kategoria wiekowa nie istnieje')

		return age_category

	def clean_cover_img(self):
		cover_img = self.cleaned_data.get('cover_img')

		if not cover_img:
			raise ValidationError('Okładka jest wymagana')

		return cover_img

	def clean(self):
		cleaned_data = super().clean()

		epub_file = cleaned_data.get('ebook_file_epub')
		mobi_file = cleaned_data.get('ebook_file_mobi')
		pdf_file = cleaned_data.get('ebook_file_pdf')

		if (not epub_file 
			and not mobi_file
			and not pdf_file):

			raise ValidationError('Musisz przesłać przynajmniej jeden plik') 

	def save(self, publisher):
		pdf_file = self.cleaned_data.get('ebook_file_pdf')
		epub_file = self.cleaned_data.get('ebook_file_epub')
		mobi_file = self.cleaned_data.get('ebook_file_mobi')
		demo_file = self.cleaned_data.get('ebook_file_demo')
		cover_img = self.cleaned_data.get('cover_img')
		category = self.cleaned_data.get('category')
		title = self.cleaned_data.get('title')
		description = self.cleaned_data.get('description')
		price = self.cleaned_data.get('price')
		author = self.cleaned_data.get('author')
		page_count = self.cleaned_data.get('page_count')
		isbn = self.cleaned_data.get('isbn')
		contents = self.cleaned_data.get('contents')
		age_category = self.cleaned_data.get('age_category')
		
		# TODO: Email o dodaniu nowego produktu do wszystkich obeserwujących danego autora 		

		product = Product.objects.create_product(publisher=publisher, category=category,
									   title=title, description=description,
									   price=price, author=author,
									   page_count=page_count, isbn=isbn,
									   contents=contents, age_category=age_category)
		
		product.pdf_file = File.objects.upload_file(pdf_file)
		product.mobi_file = File.objects.upload_file(mobi_file)
		product.epub_file = File.objects.upload_file(epub_file)
		product.demo_file = File.objects.upload_file(demo_file)

		product.cover_img = File.objects.upload_file(cover_img)

		product.save()