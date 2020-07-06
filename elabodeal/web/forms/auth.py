from django import forms
from django.core.validators import EmailValidator

from elabodeal.models import User


class LoginForm(forms.Form):
	email=forms.EmailField(
		widget=forms.TextInput(attrs={
			'class': 'form__input'}),
		error_messages={
			'invalid': 'Podaj poprawny email',
			'required': ''}
	)

	password = forms.CharField(
		widget=forms.PasswordInput(attrs={
			'class': 'form__input'}),
		error_messages={'required': ''}
	)


class RegisterForm(forms.Form):
	username = forms.CharField(
		max_length=30,
		widget=forms.TextInput(attrs={
			'class': 'form__input'}),
		error_messages={'required': ''}
	)

	email=forms.EmailField(
		widget=forms.TextInput(attrs={
			'class': 'form__input'}),
		error_messages={
			'invalid': 'Podaj poprawny email',
			'required': ''}
	)

	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={
			'class': 'form__input'}),
		error_messages={'required': ''}
	)

	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={
			'class': 'form__input'}),
		error_messages={'required': ''}
	)

	def clean_password2(self):
		password1 = self.cleaned_data['password1']
		password2 = self.cleaned_data['password2']
		if(password1 != password2):
			self.add_error('password2', 'Hasła nie są takie same')

		return password2

	def clean_username(self):
		username = self.cleaned_data['username']
		user = User.objects.filter(username=username).first()
		if user:
			self.add_error('username', 'Nazwa użytkownika jest zajęta')

		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		user = User.objects.filter(email=email).first()
		if user:
			self.add_error('email', 'Email jest zajęty')

		return email

	def save(self):
		user = User()
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']
		user.set_password(self.cleaned_data['password2'])
		user.save()
