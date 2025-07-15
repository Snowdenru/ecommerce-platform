from celery import shared_task
import time
from .models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string



@shared_task
def add(x, y):
    time.sleep(10)
    print("СЛОЖЕНИЕ ЧИСЕЛ!!!!!")
    return x + y


@shared_task
def sens_verification_email(user_id):
    user = User.objects.get(id=user_id)
    subject = "Подтвердите ваш почтовый ящик"
    message = render_to_string('account/email_verification.html', {
        'user': user,
        'uid': '',
        'token': ''
    })
    send_mail(
        subject,
        message,
        setting.DEFALT_FROM_EMAIL,
        fail_silently=False
    )

