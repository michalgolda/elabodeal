from tests import BaseTestCase

from django.core import mail
from django.test import override_settings
from django.template.loader import render_to_string

from elabodeal.emails import (
    Email,
    ConfirmEmailChangeEmail,
    PurchaseConfirmationEmail,
    ResetPasswordRequestEmail,
    UserRegisterConfirmationEmail,
    PublishedProductInformationEmail,
)


class UserRegisterConfirmationEmailTest(BaseTestCase):
    
    @override_settings(
		task_always_eager=True,
		EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
	)
    def test_simple(self):
        mail.outbox = []

        email_to = 'test@test.pl'
        email_template_context = {
            'code': 123123
        }
        
        email = UserRegisterConfirmationEmail(
            to=email_to,
            template_context=email_template_context
        )
        email.send()

        email_sent = mail.outbox[0]
        email_sent_alternative = email_sent.alternatives[0]
        email_sent_alternative_content = email_sent_alternative[0]
        email_sent_alternative_mime_type = email_sent_alternative[1]

        self.assertEqual(
            email_sent_alternative_content, 
            render_to_string(
                'emails/user-register-confirmation.html',
                email_template_context
            )
        )
        self.assertEqual(email_sent.to, ['test@test.pl'])
        self.assertEqual(email_sent_alternative_mime_type, 'text/html')
        self.assertEqual(email_sent.subject, 'Elabodeal - Potwierdzenie rejestracji')


class ConfirmEmailChangeEmailTest(BaseTestCase):
    
    @override_settings(
		task_always_eager=True,
		EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
	)
    def test_simple(self):
        mail.outbox = []
        
        email_to = 'test@test.pl'
        email_template_context = {
            'code': 123123
        }

        email = ConfirmEmailChangeEmail(
            to=email_to,
            template_context=email_template_context
        )
        email.send()

        self.assertEqual(len(mail.outbox), 1)

        email_sent = mail.outbox[0]
        email_sent_alternative = email_sent.alternatives[0]
        email_sent_alternative_content = email_sent_alternative[0]
        email_sent_alternative_mime_type = email_sent_alternative[1]

        self.assertEqual(
            email_sent_alternative_content, 
            render_to_string(
                'emails/confirm-email-change.html',
                email_template_context
            )
        )
        self.assertEqual(email_sent.to, ['test@test.pl'])
        self.assertEqual(email_sent_alternative_mime_type, 'text/html')
        self.assertEqual(email_sent.subject, 'Elabodeal - Kod weryfikacyjny')



class PurchaseConfirmationEmailTest(BaseTestCase):
    
    @override_settings(
		task_always_eager=True,
		EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
	)
    def test_simple(self):
        mail.outbox = []
        
        email_to = 'test@test.pl'
        email_template_context = {
            'total_price': 12.00,
            'buyer_first_name': 'test',
            'purchased_products': [],
            'userIsAuthenticated': True
        }

        email = PurchaseConfirmationEmail(
            to=email_to,
            template_context=email_template_context
        )
        email.send()

        self.assertEqual(len(mail.outbox), 1)

        email_sent = mail.outbox[0]
        email_sent_alternative = email_sent.alternatives[0]
        email_sent_alternative_content = email_sent_alternative[0]
        email_sent_alternative_mime_type = email_sent_alternative[1]

        self.assertEqual(
            email_sent_alternative_content, 
            render_to_string(
                'emails/purchase-confirmation.html',
                email_template_context
            )
        )
        self.assertEqual(email_sent.to, ['test@test.pl'])
        self.assertEqual(email_sent_alternative_mime_type, 'text/html')
        self.assertEqual(email_sent.subject, 'Elabodeal - Potwierdzenie płatnośći')


class PublishedProductInformationEmailTest(BaseTestCase):
    
    @override_settings(
		task_always_eager=True,
		EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
	)
    def test_simple(self):
        mail.outbox = []
        
        email_to = 'test@test.pl'
        email_template_context = {
            'title': 'test',
            'price': 12.00,
            'author': 'test',
            'cover_img_path': 'test'
        }
        
        email = PublishedProductInformationEmail(
            to=email_to,
            template_context=email_template_context
        )
        email.send()

        self.assertEqual(len(mail.outbox), 1)

        email_sent = mail.outbox[0]
        email_sent_alternative = email_sent.alternatives[0]
        email_sent_alternative_content = email_sent_alternative[0]
        email_sent_alternative_mime_type = email_sent_alternative[1]

        self.assertEqual(
            email_sent_alternative_content, 
            render_to_string(
                'emails/published-product-information.html',
                email_template_context
            )
        )
        self.assertEqual(email_sent.to, ['test@test.pl'])
        self.assertEqual(email_sent_alternative_mime_type, 'text/html')
        self.assertEqual(email_sent.subject, 'Elabodeal - Wystawienie produktu na rynek')


class ResetPasswordRequestEmailTest(BaseTestCase):

    @override_settings(
		task_always_eager=True,
		EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
	)
    def test_simple(self):
        mail.outbox = []
        
        email_to = 'test@test.pl'
        email_template_context = {
            'code': '123123'
        }
        
        email = ResetPasswordRequestEmail(
            to=email_to,
            template_context=email_template_context
        )
        email.send()

        self.assertEqual(len(mail.outbox), 1)

        email_sent = mail.outbox[0]
        email_sent_alternative = email_sent.alternatives[0]
        email_sent_alternative_content = email_sent_alternative[0]
        email_sent_alternative_mime_type = email_sent_alternative[1]

        self.assertEqual(
            email_sent_alternative_content, 
            render_to_string(
                'emails/reset-password-request.html',
                email_template_context
            )
        )
        self.assertEqual(email_sent.to, ['test@test.pl'])
        self.assertEqual(email_sent_alternative_mime_type, 'text/html')
        self.assertEqual(email_sent.subject, 'Elabodeal - Resetowanie hasła')