from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login

from elabodeal.celery.tasks import send_email
from elabodeal.models import User, VerificationCode
from elabodeal.emails import UserRegisterConfirmationEmail


class LoginForm(forms.Form):

    def __init__(self, request = None, *args, **kwargs):
        self.request = request

        request_post_data = request.POST if request else None

        super(LoginForm, self).__init__(request_post_data, *args, **kwargs)

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form__input'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form__input'
            }
        )
    )

    def clean(self):
        super().clean()

        user_email = self.cleaned_data['email']
        user_password = self.cleaned_data['password']

        user = authenticate(
            self.request,
            email=user_email,
            password=user_password
        )

        if not user:
            raise ValidationError(
                _('Nieprawdiłowy email lub hasło')
            )

        self.cleaned_data['user'] = user

        return self.cleaned_data

    def execute(self):
        user = self.cleaned_data['user']

        login(self.request, user)


class RegisterForm(forms.Form):
    
    def __init__(self, request = None, *args, **kwargs):
        request_post_data = request.POST if request else None

        super(RegisterForm, self).__init__(request_post_data, *args, **kwargs)

    username = forms.CharField(
        max_length=User.MAX_USERNAME_LENGTH,
        widget=forms.TextInput(
            attrs={
                'class': 'form__input'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form__input'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form__input'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form__input'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']

        existing_user = User.objects.filter(username=username).first()

        if existing_user:
            raise ValidationError(
                _('Podana nazwa użytkownika jest w użyciu')
            )

        return username

    def clean_email(self):
        email = self.cleaned_data['email']

        existing_user = User.objects.filter(email=email).first()

        if existing_user:
            raise ValidationError(
                _('Podany adres email jest w użyciu')
            )

        return email

    def clean(self):
        super().clean()

        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            self.add_error(
                'password',
                _('Hasła nie są takie same')
            )

        self.cleaned_data['password'] = password1

        return self.cleaned_data

    def execute(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        # User.objects.create_user(
        #     email,
        #     username,
        #     password
        # )

        created_verification_code = VerificationCode.objects.create_code(email)

        user_register_confirmation_email = UserRegisterConfirmationEmail(
            to=email,
            template_context={
                'code': created_verification_code.code
            }
        )
        user_register_confirmation_email.send()