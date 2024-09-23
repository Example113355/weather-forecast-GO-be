from django.core.mail import send_mail
from django.conf import settings
from typing import List
from ..exceptions import EmailServiceError

class MailService:
    @staticmethod
    def send_mail(subject: str, message: str, recipient: str):
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
            return True
        except Exception:
            raise EmailServiceError()
