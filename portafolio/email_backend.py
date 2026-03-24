"""
Custom email backend that uses the HTTP mailer API
"""

import requests
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend


class HTTPMailerBackend(BaseEmailBackend):
    """
    Email backend that sends emails via the servicomf5-mailer HTTP API
    """

    def __init__(self, fail_silently=False, **kwargs):
        self.fail_silently = fail_silently
        self.mailer_url = getattr(
            settings, "MAILER_URL", "http://servicomf5-mailer:8001/mailer/send"
        )

    def send_messages(self, messages):
        """
        Send messages via the HTTP mailer API
        """
        if not messages:
            return 0

        sent_count = 0
        for message in messages:
            if message.to:
                for recipient in message.to:
                    try:
                        self._send_via_api(
                            to=recipient,
                            subject=message.subject,
                            body=message.body,
                            from_email=message.from_email
                            or settings.DEFAULT_FROM_EMAIL,
                        )
                        sent_count += 1
                    except Exception as e:
                        if not self.fail_silently:
                            raise
        return sent_count

    def _send_via_api(self, to, subject, body, from_email):
        """
        Send email via HTTP API
        """
        payload = {"to": to, "subject": subject, "body": body}

        response = requests.post(self.mailer_url, json=payload, timeout=30)

        if response.status_code not in (200, 201):
            raise Exception(
                f"Mailer API error: {response.status_code} - {response.text}"
            )
