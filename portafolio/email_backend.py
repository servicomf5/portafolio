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
            settings, "MAILER_URL", "http://172.21.0.4:8001/mailer/send"
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
        Send email via HTTP API with HTML template
        """
        # Extract sender email from body for reply-to
        sender_email = ""
        for line in body.split("\n"):
            if line.startswith("De:"):
                import re

                email_match = re.search(r"<(.+?)>", line)
                if email_match:
                    sender_email = email_match.group(1)
                break

        # Create HTML email template
        html_body = self._create_html_email(subject, body)

        payload = {"to": to, "subject": subject, "body": html_body}

        # Add reply-to if we have sender email
        if sender_email:
            payload["from_email"] = sender_email

        response = requests.post(self.mailer_url, json=payload, timeout=30)

        if response.status_code not in (200, 201):
            raise Exception(
                f"Mailer API error: {response.status_code} - {response.text}"
            )

    def _create_html_email(self, subject, body):
        """
        Create a nice HTML email template
        """
        # Parse the plain text body to extract info
        lines = body.split("\n")
        from_line = ""
        from_email = ""
        message_content = body

        for line in lines:
            if line.startswith("De:"):
                from_line = line.replace("De:", "").strip()
                # Extract email from format "nombre <email>"
                import re

                email_match = re.search(r"<(.+?)>", from_line)
                if email_match:
                    from_email = email_match.group(1)
                    # Also extract just the name
                    from_name = re.sub(r"<.+?>", "", from_line).strip()
                    from_line = f"{from_name} &lt;{from_email}&gt;"
            elif line.startswith("Mensaje:"):
                idx = body.find(line)
                message_content = body[idx + len(line) :].strip()

        return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333333;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            background: linear-gradient(135deg, #f9a826 0%, #f5a623 100%);
            color: #ffffff;
            padding: 30px 20px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 24px;
            font-weight: 600;
        }}
        .header .subtitle {{
            margin: 5px 0 0 0;
            font-size: 14px;
            opacity: 0.9;
        }}
        .content {{
            padding: 30px;
        }}
        .info-box {{
            background-color: #f9f9f9;
            border-left: 4px solid #f9a826;
            padding: 15px 20px;
            margin-bottom: 20px;
            border-radius: 0 4px 4px 0;
        }}
        .info-row {{
            margin-bottom: 10px;
        }}
        .info-label {{
            font-weight: 600;
            color: #555;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .info-value {{
            color: #333;
            font-size: 16px;
        }}
        .message-box {{
            background-color: #fff;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            padding: 20px;
            margin-top: 15px;
        }}
        .message-text {{
            white-space: pre-wrap;
            word-wrap: break-word;
            color: #444;
            line-height: 1.8;
        }}
        .footer {{
            background-color: #f5f5f5;
            padding: 20px;
            text-align: center;
            font-size: 12px;
            color: #888;
        }}
        .footer a {{
            color: #f9a826;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📬 Nuevo Mensaje de Contacto</h1>
            <p class="subtitle">Portfolio Eduardo Muñoz</p>
        </div>
        <div class="content">
            <div class="info-box">
                <div class="info-row">
                    <span class="info-label">Remitente</span>
                    <p class="info-value">{from_line if from_line else "No especificado"}</p>
                </div>
                {f'<div class="info-row"><span class="info-label">Email</span><p class="info-value"><a href="mailto:{from_email}">{from_email}</a></p></div>' if from_email else ""}
            </div>
            <div class="message-box">
                <span class="info-label">Mensaje</span>
                <p class="message-text">{message_content}</p>
            </div>
        </div>
        <div class="footer">
            <p>Este mensaje fue enviado desde el formulario de contacto de tu portfolio.</p>
            <p><a href="https://portafolio.servicomf5.cl">portafolio.servicomf5.cl</a></p>
        </div>
    </div>
</body>
</html>
"""
