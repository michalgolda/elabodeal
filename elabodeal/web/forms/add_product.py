from django import forms

from elabodeal.models import Category

LANG_CHOICES = [
	('1', 'Polski'),
	('1', 'Niemiecki'),
	('1', 'Angielski')
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

	epub = forms.FileField()

	pdf = forms.FileField()

	mobi = forms.FileField()

	accept_rules = forms.ChoiceField(
		widget=forms.CheckboxInput(
			attrs={'class': 'float-left'}
		)
	)

