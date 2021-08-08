from elabodeal.celery.tasks import send_email
from django.template.loader import render_to_string


class Email:
    subject = None
    template = None

    def __init__(self, to, text_message = None, template_context = None):
        self.to = to
        self.text_message = text_message
        self.template_context = template_context

    def send(self):
        html_message = render_to_string(
            self.template,
            self.template_context
        ) if self.template else None

        send_email.delay({
            'to': self.to,
            'subject': self.subject,
            'html_message': html_message,
            'text_message': self.text_message
        })


class UserRegisterConfirmationEmail(Email):
    template = 'emails/user-register-confirmation.html'
    subject = 'Elabodeal - Potwierdzenie rejestracji'


class ConfirmEmailChangeEmail(Email):
    subject = 'Elabodeal - Kod weryfikacyjny'
    template = 'emails/confirm-email-change.html'


class PurchaseConfirmationEmail(Email):
    subject = 'Elabodeal - Potwierdzenie płatnośći'
    template = 'emails/purchase-confirmation.html'


class PublishedProductInformationEmail(Email):
    subject = 'Elabodeal - Wystawienie produktu na rynek'
    template = 'emails/published-product-information.html'