from dataclasses import dataclass, field


@dataclass
class EmailDTO:
    to: str
    context: dict
    subject: str = field(init=False, default=None)
    template: str = field(init=False, default=None)
    text_message: str = field(init=False, default=None)

    def asdict(self):
        return {
            'to': self.to,
            'context': self.context,
            'subject': self.subject,
            'template': self.template,
            'text_message': self.text_message
        }


class ConfirmEmailChangeEmailDTO(EmailDTO):
    subject = 'Elabodeal - Kod weryfikacyjny'
    template = 'emails/confirm-email-change.html'


class ConfirmNewUserEmail(EmailDTO):
    subject = 'Elabodeal - Potwierdzenie rejestracji'
    template = 'emails/confirm-new-user.html'


class PurchaseConfirmationEmailDTO(EmailDTO):
    subject = 'Elabodeal - Potwierdzenie płatnośći'
    template = 'emails/purchase-confirmation.html'