from tests import BaseTestCase
from elabodeal.emails import (
    EmailDTO,
    ConfirmEmailChangeEmailDTO,
    PurchaseConfirmationEmailDTO,
    UserRegisterConfirmationEmailDTO,
    PublishedProductInformationEmailDTO
)


class EmailDTOTest(BaseTestCase):
    def test_simple(self):
        email_dto = EmailDTO(
            to='test@test.pl',
            template_context=None
        )
        email_dto.subject = 'test'
        email_dto.text_message = 'test'

        serialized_email_dto = email_dto.serialize()

        self.assertEqual(serialized_email_dto, {
            'to': email_dto.to,
            'subject': email_dto.subject,
            'text_message': email_dto.text_message,
            'html_message': None
        })


class ConfirmEmailChangeEmailDTOTest(BaseTestCase):
    def test_simple(self):
        email_dto = ConfirmEmailChangeEmailDTO(
            to='test@test.pl',
            template_context=None
        )

        serialized_email_dto = email_dto.serialize()

        self.assertNotEqual(serialized_email_dto.get('html_message'), None)
        self.assertEqual(email_dto.subject, 'Elabodeal - Kod weryfikacyjny')
        self.assertEqual(email_dto.template, 'emails/confirm-email-change.html')


class UserRegisterConfirmationEmailDTOTest(BaseTestCase):
    def test_simple(self):
        email_dto = UserRegisterConfirmationEmailDTO(
            to='test@test.pl',
            template_context=None
        )

        serialized_email_dto = email_dto.serialize()

        self.assertNotEqual(serialized_email_dto.get('html_message'), None)
        self.assertEqual(email_dto.subject, 'Elabodeal - Potwierdzenie rejestracji')
        self.assertEqual(email_dto.template, 'emails/user-register-confirmation.html')


class PurchaseConfirmationEmailDTOTest(BaseTestCase):
    def test_simple(self):
        email_dto = PurchaseConfirmationEmailDTO(
            to='test@test.pl',
            template_context=None
        )

        serialized_email_dto = email_dto.serialize()

        self.assertNotEqual(serialized_email_dto.get('html_message'), None)
        self.assertEqual(email_dto.subject, 'Elabodeal - Potwierdzenie płatnośći')
        self.assertEqual(email_dto.template, 'emails/purchase-confirmation.html')


class PublishedProductInformationEmailDTOTest(BaseTestCase):
    def test_simple(self):
        email_dto = PublishedProductInformationEmailDTO(
            to='test@test.pl',
            template_context=None
        )

        serialized_email_dto = email_dto.serialize()

        self.assertNotEqual(serialized_email_dto.get('html_message'), None)
        self.assertEqual(email_dto.subject, 'Elabodeal - Wystawienie produktu na rynek')
        self.assertEqual(email_dto.template, 'emails/published-product-information.html')
