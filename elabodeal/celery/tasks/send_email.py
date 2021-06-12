from django.core.mail import send_mail
from django.template.loader import render_to_string

from elabodeal.celery import app


@app.task(name='send_email')
def send_email(serialized_email_dto):
    to = serialized_email_dto.get('to')
    subject = serialized_email_dto.get('subject')
    context = serialized_email_dto.get('context')
    template = serialized_email_dto.get('template')
    message = serialized_email_dto.get('text_message')
    html_message = render_to_string(
        template,
        context
    )

    send_mail(
        from_email=None,
        message=message,
        subject=subject,
        recipient_list=[to],
        html_message=html_message
    )