from django import forms
from elabodeal.models import Publisher


COUNTRY_CHOICES = (
	("1", "Polska"),
	("2", "Niemcy"))

class StartSellingForm(forms.Form):
	country = forms.ChoiceField(
		choices=COUNTRY_CHOICES,
		widget=forms.Select)

	swift = forms.CharField(widget=forms.TextInput)

	account_number = forms.CharField(widget=forms.TextInput)

	first_name = forms.CharField(widget=forms.TextInput)

	last_name = forms.CharField(widget=forms.TextInput)

	sell_notification = forms.BooleanField(
		required=False,
		widget=forms.CheckboxInput())

	def save(self, user):
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		country = self.cleaned_data.get('country')
		swift = self.cleaned_data.get('swift')
		account_number = self.cleaned_data.get('account_number')
		sell_notification = self.cleaned_data.get('sell_notification')

		publisher = Publisher.objects.create_publisher(first_name=first_name, 
													   last_name=last_name,
													   country=country,
													   swift=swift,
													   account_number=account_number,
													   sell_notification=sell_notification)
		
		user.publisher = publisher
		user.save()

