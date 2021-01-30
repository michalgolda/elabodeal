from django.core.mail import send_mail
from django.template.loader import render_to_string

from elabodeal.celery import app


@app.task(name='send_email')
def send_email(email: dict) -> None:
    send_mail(
        from_email=None,
        message=email['text_message'],
        subject=email['subject'],
        recipient_list=[email['to']],
        html_message=render_to_string(
            email['template'],
            email['context']
        )
    )