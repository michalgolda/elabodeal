from django import forms


class DeliveryForm(forms.Form):
	first_name = forms.CharField(
		widget=forms.TextInput,
	)

	last_name = forms.CharField(
		widget=forms.TextInput,
	)

	email = forms.EmailField(
		widget=forms.TextInput,
		error_messages={
			'invalid': 'Podaj poprawny email',
			'required': ''}
	)