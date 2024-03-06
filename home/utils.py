
import time

from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject = "Test Email from django server"
    message = "This email was sent by using Django as a test mail."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["receiver@gmail.com"]

    send_mail(subject , message , from_email , recipient_list)