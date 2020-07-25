from django import forms

from elabodeal.models import Category

LANG_CHOICES = [
	('1', 'Polski'),
	('2', 'Niemiecki'),
	('3', 'Angielski')
]

class AddProductForm(forms.Form):
	lang = forms.ChoiceField(
		choices=LANG_CHOICES,
		widget=forms.Select,
	)

	table_of_content = forms.CharField(
		widget=forms.Textarea,
	)

	title = forms.CharField(
		widget=forms.TextInput
	)

	description = forms.CharField(
		widget=forms.Textarea,
	)

	author = forms.CharField(
		widget=forms.TextInput
	)

	isbn = forms.CharField(
		widget=forms.TextInput
	)

	page_count = forms.IntegerField(
		widget=forms.NumberInput(
			attrs={'min': '1'}
		),
	)

	price = forms.DecimalField(
		widget=forms.NumberInput(
			attrs={'min': '1'}
		),
	)

	copies = forms.IntegerField(
		widget=forms.NumberInput
	)

	epub_file = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'ebook-file-input', 'accept': '.epub'}
		)
	)

	pdf_file = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'ebook-file-input', 'accept': '.pdf'}
		)
	)

	mobi_file = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'ebook-file-input', 'accept': '.mobi'}
		)
	)

	demo_pdf_file = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'ebook-file-input', 'accept': '.pdf'}
		)
	)

	age_0 = forms.BooleanField(
		required=False,
		widget=forms.CheckboxInput(
			attrs={'id': 'age-choice-input'}
		)
	)

	age_1 = forms.BooleanField(
		required=False,
		widget=forms.CheckboxInput(
			attrs={'id': 'age-choice-input'}
		)
	)

	age_2 = forms.BooleanField(
		required=False,
		widget=forms.CheckboxInput(
			attrs={'id': 'age-choice-input'}
		)
	)

	age_3 = forms.BooleanField(
		required=False,
		widget=forms.CheckboxInput(
			attrs={'id': 'age-choice-input'}
		)
	)

	age_4 = forms.BooleanField(
		required=False,
		widget=forms.CheckboxInput(
			attrs={'id': 'age-choice-input'}
		)
	)

	file_image_0 = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	file_image_1 = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	file_image_2 = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	file_image_3 = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	file_image_4 = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	file_image_5 = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	file_image_6 = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	file_image_7 = forms.FileField(
		required=False,
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)
	
	accept_rules = forms.BooleanField(
		widget=forms.CheckboxInput(
			attrs={'class': 'float-left'}
		)
	)

