from dataclasses import dataclass, field
from django.template.loader import render_to_string


@dataclass
class EmailDTO:
    to: str
    template_context: dict
    subject: str = field(init=False, default=None)
    template: str = field(init=False, default=None)
    text_message: str = field(init=False, default=None)

    def serialize(self):
        html_message = render_to_string(
            self.template,
            self.template_context
        ) if self.template else None

        return {
            'to': self.to,
            'subject': self.subject,
            'text_message': self.text_message,
            'html_message': html_message
        }


class ConfirmEmailChangeEmailDTO(EmailDTO):
    subject = 'Elabodeal - Kod weryfikacyjny'
    template = 'emails/confirm-email-change.html'


class UserRegisterConfirmationEmailDTO(EmailDTO):
    subject = 'Elabodeal - Potwierdzenie rejestracji'
    template = 'emails/user-register-confirmation.html'


class PurchaseConfirmationEmailDTO(EmailDTO):
    subject = 'Elabodeal - Potwierdzenie płatnośći'
    template = 'emails/purchase-confirmation.html'


class PublishedProductInformationEmailDTO(EmailDTO):
    subject = 'Elabodeal - Wystawienie produktu na rynek'
    template = 'emails/published-product-information.html'