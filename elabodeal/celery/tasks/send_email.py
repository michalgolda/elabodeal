from django.core.mail import send_mail

from elabodeal.celery import app


@app.task(name='send_email')
def send_email(serialized_email_dto):
    to = serialized_email_dto.get('to')
    subject = serialized_email_dto.get('subject')
    message = serialized_email_dto.get('text_message')
    html_message = serialized_email_dto.get('html_message')

    send_mail(
        from_email=None,
        message=message,
        subject=subject,
        recipient_list=[to],
        html_message=html_message
    )