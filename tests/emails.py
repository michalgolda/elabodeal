from tests import BaseTestCase

from elabodeal.emails import (
    Email, 
    ConfirmChangeEmail, 
    ConfirmNewUserEmail
)


class TestEmail(BaseTestCase):
    def test_simple(self):
        email = Email(
            to='test',
            context=None
        )

        self.assertEqual(hasattr(email, 'to'), True)
        self.assertEqual(hasattr(email, 'context'), True)
        self.assertEqual(hasattr(email, 'subject'), True)
        self.assertEqual(hasattr(email, 'template'), True)
        self.assertEqual(hasattr(email, 'text_message'), True)

    def test_asdict_method(self):
        email = Email(
            to='test',
            context=None,
        )

        email.template = 'test'
        email.subject = 'test'
        email.text_message = 'test'

        self.assertEqual(
            email.asdict(), 
            {
                'to': 'test',
                'subject': 'test',
                'template': 'test',
                'text_message': 'test',
                'context': None
            }
        )


class TestConfirmChangeEmail(BaseTestCase):
    def test_default_params(self):
        email = ConfirmChangeEmail(
            to='test',
            context=None
        )

        self.assertEqual(
            email.subject, 
            'Elabodeal - Kod weryfikacyjny'
        )
        self.assertEqual(
            email.template,
            'emails/confirm-change-email.html'    
        )


class TestConfirmNewUserEmail(BaseTestCase):
    def test_default_params(self):
        email = ConfirmNewUserEmail(
            to='test',
            context=None
        )

        self.assertEqual(
            email.subject, 
            'Elabodeal - Potwierdzenie rejestracji'
        )
        self.assertEqual(
            email.template,
            'emails/confirm-new-user.html'    
        )