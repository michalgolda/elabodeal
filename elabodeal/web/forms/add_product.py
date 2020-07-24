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

	epub = forms.FileField(
		widget=forms.FileInput(
			attrs={'id': 'ebook-file-input', 'accept': '.epub'}
		)
	)

	pdf = forms.FileField(
		widget=forms.FileInput(
			attrs={'id': 'ebook-file-input', 'accept': '.pdf'}
		)
	)

	mobi = forms.FileField(
		widget=forms.FileInput(
			attrs={'id': 'ebook-file-input', 'accept': '.mobi'}
		)
	)

	demo_pdf = forms.FileField(
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

	image_0 = forms.FileField(
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	image_1 = forms.FileField(
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	image_2 = forms.FileField(
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	image_3 = forms.FileField(
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	image_4 = forms.FileField(
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	image_5 = forms.FileField(
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	image_6 = forms.FileField(
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)

	image_7 = forms.FileField(
		widget=forms.FileInput(
			attrs={'id': 'image-file-input', 'accept': 'images/*'}
		)
	)
	
	accept_rules = forms.ChoiceField(
		widget=forms.CheckboxInput(
			attrs={'class': 'float-left'}
		)
	)

