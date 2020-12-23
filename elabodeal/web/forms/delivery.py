from django import forms


class DeliveryForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput)

	last_name = forms.CharField(widget=forms.TextInput)

	email = forms.EmailField(widget=forms.TextInput,
							 error_messages={
								'invalid': 'Podaj poprawny email',
								'required': ''})

	gift = forms.BooleanField(required=False,
							  widget=forms.CheckboxInput(
								attrs={'class': 'float-left', 
								       'id': 'show-gift-form'}))

	gift_first_name = forms.CharField(required=False,
									  widget=forms.TextInput)

	gift_last_name = forms.CharField(required=False,
									 widget=forms.TextInput)

	gift_email = forms.EmailField(required=False,
								  widget=forms.TextInput,
								  error_messages={
									'invalid': 'Podaj poprawny email',
									'required': ''})
		