from django import forms

from elabodeal.models import Category

CATEGORY_CHOICES = [(c.id, c.name) for c in Category.objects.all()]

class AddProductForm(forms.Form):
	title = forms.CharField(
		widget=forms.TextInput(
			attrs={'class': 'form__input'}
		)
	)

	category = forms.ChoiceField(
		choices=CATEGORY_CHOICES,
		widget=forms.Select(
			attrs={
			'class': 'form__input'}
		),
	)

	description = forms.CharField(
		widget=forms.Textarea(
			attrs={'class': 'form__input'}
		),
	)

	page_count = forms.IntegerField(
		widget=forms.NumberInput(
			attrs={'class': 'form__input', 'min': '1'}
		),
	)

	price = forms.DecimalField(
		widget=forms.NumberInput(
			attrs={'class': 'form__input', 'min': '1'}
		),
	)

	cover_img_url = forms.URLField(
		widget=forms.URLInput(
			attrs={'class': 'form__input'}
		),
	)