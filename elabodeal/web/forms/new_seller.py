from django import forms

COUNTRY_CHOICES = (
	("1", "Polska"),
	("2", "Niemcy")
)

class NewSellerForm(forms.Form):
	country = forms.ChoiceField(
		choices=COUNTRY_CHOICES,
		widget=forms.Select,
	)

	swift = forms.CharField(
		widget=forms.TextInput,
	)

	account_number = forms.CharField(
		widget=forms.TextInput,
	)

	first_name = forms.CharField(
		widget=forms.TextInput,
	)

	last_name = forms.CharField(
		widget=forms.TextInput,
	)

	notify_when_buy_book = forms.ChoiceField(
		widget=forms.CheckboxInput(
			attrs={
				'class': 'float-left'
			}
		)
	)

	notify_when_withdraw = forms.ChoiceField(
		widget=forms.CheckboxInput(
			attrs={
				'class': 'float-left'
			}
		),
	)

