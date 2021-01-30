from dataclasses import dataclass, field


@dataclass
class Email:
    to: str
    context: dict
    text_message: str = field(init=False, default=None)
    subject: str = field(init=False, default=None)
    template: str = field(init=False, default=None)

    def asdict(self) -> dict:
        return {
            'to': self.to,
            'context': self.context,
            'text_message': self.text_message,
            'subject': self.subject,
            'template': self.template
        }


class ConfirmChangeEmail(Email):
    subject = 'Elabodeal - Kod weryfikacyjny'
    template = 'emails/confirm-change-email.html'


class ConfirmNewUserEmail(Email):
    subject = 'Elabodeal - Potwierdzenie rejestracji'
    template = 'emails/confirm-new-user.html'