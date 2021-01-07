from django.conf import settings
from django.core.mail import send_mail

from send_email.celery import app
from .models import Contact
from .service import send


@app.task
def send_spam_email(user_email):
    send(user_email)

@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Мы будем присылать Вам много спама каждые 5 минут',
            settings.EMAIL_HOST_USER,
            [contact.email],
            fail_silently=False,
        )
