from django import forms
from django.core.validators import MaxLengthValidator


class EmailVerificationForm(forms.Form):
	code=forms.CharField(
		widget=forms.TextInput(
			attrs={
			'class': 'form__input',
			'maxlength': 6,
			'oninput': "this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"}))

	def clean_code(self):
		code = self.cleaned_data.get('code')

		if len(code) != 6:
			self.add_error(
				'code', 
				'Niepoprawny kod weryfikacyjny. Spróbuj ponownie.')

		return code