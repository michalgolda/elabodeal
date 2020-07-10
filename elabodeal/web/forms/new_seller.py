from django import forms

COUNTRY_CHOICES = (
	("1", "Polska"),
	("2", "Niemcy")
)

class NewSellerForm(forms.Form):
	country = forms.ChoiceField(
		choices=COUNTRY_CHOICES,
		widget=forms.Select(attrs={
			'class': 'form__input'
		}),
	)

	swift = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form__input'
		}),
	)

	account_number = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form__input'
		}),
	)

	first_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form__input'
		}),
	)

	last_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form__input'
		}),
	)

	notify_when_buy_book = forms.ChoiceField(
		widget=forms.CheckboxInput(
			attrs={
				'class': 'form__input--checkbox display-inline-block'
			}
		)
	)

	notify_when_withdraw = forms.ChoiceField(
		widget=forms.CheckboxInput(
			attrs={
				'class': 'form__input--checkbox display-inline-block'
			}
		)
	)

