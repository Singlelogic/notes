# from django.core.mail import send_mail
from send_email.celery import app

# from .models import Contact
from .service import send


@app.task
def send_spam_email(user_email):
    send(user_email)