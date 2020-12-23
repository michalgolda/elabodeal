from django import forms

from elabodeal.models import User, VerificationCode


class LoginForm(forms.Form):
	email=forms.EmailField(
		widget=forms.TextInput(
			attrs={'class': 'form__input'}),
		error_messages={'invalid': 'Podaj poprawny email'})

	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form__input'}))


class RegisterForm(forms.Form):
	username = forms.CharField(
		max_length=30,
		widget=forms.TextInput(attrs={'class': 'form__input'}))

	email=forms.EmailField(
		widget=forms.TextInput(attrs={'class': 'form__input'})
	)

	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form__input'})
	)

	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form__input'})
	)

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		
		if password1 != password2:
			self.add_error(
				'password2', 
				'Hasła nie są takie same')

		return password2

	def clean_username(self):
		username = self.cleaned_data.get('username')
		
		user = User.objects.filter(username=username).first()
		
		if user:
			self.add_error(
				'username', 
				'Nazwa użytkownika jest zajęta')

		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
	
		user = User.objects.filter(email=email).first()
	
		if user:
			self.add_error(
				'email', 
				'Podany adres email jest zajęty')

		return email

	def save(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password1')

		User.objects.create_user(email, username, password)

		VerificationCode.objects.generate(email)
