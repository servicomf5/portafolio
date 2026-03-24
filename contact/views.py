from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views.generic import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from django.conf import settings
from portfolio.models import Profile
from .forms import ContactForm


class ContactView(FormView):
    """Vista para el formulario de contacto."""

    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def get_context_data(self, **kwargs):
        """Agrega el perfil al contexto."""
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context

    def form_valid(self, form):
        """Envía el email cuando el formulario es válido."""
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        subject = form.cleaned_data.get("subject", "Sin asunto")
        message = form.cleaned_data["message"]

        # Obtener nombre del propietario del portafolio
        profile = Profile.objects.first()
        owner_name = (
            f"{profile.first_name} {profile.last_name}" if profile else "el propietario"
        )

        # Enviar email HTML
        recipient = getattr(settings, "CONTACT_EMAIL", "email@ejemplo.com")

        # Versión texto plano
        text_content = f"""
Nuevo mensaje desde el portafolio de {owner_name}.

De: {name} <{email}>
Asunto: {subject}

Mensaje:
{message}
"""

        # Versión HTML
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f5f5f5; padding: 20px; }}
        .container {{ max-width: 600px; margin: 0 auto; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .header {{ background: #f9a826; color: #fff; padding: 20px; text-align: center; }}
        .header h1 {{ margin: 0; font-size: 24px; }}
        .content {{ padding: 20px; }}
        .label {{ font-weight: bold; color: #333; }}
        .value {{ color: #555; margin-bottom: 10px; }}
        .message-box {{ background: #f9f9f9; padding: 15px; border-left: 4px solid #f9a826; margin-top: 15px; white-space: pre-wrap; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📬 Nuevo mensaje del Portfolio</h1>
        </div>
        <div class="content">
            <p class="label">De:</p>
            <p class="value">{name} &lt;{email}&gt;</p>
            
            <p class="label">Asunto:</p>
            <p class="value">{subject}</p>
            
            <p class="label">Mensaje:</p>
            <div class="message-box">{message}</div>
        </div>
    </div>
</body>
</html>
"""

        # Enviar email con ambas versiones
        msg = EmailMultiAlternatives(
            subject=f"[Portafolio Contacto] {subject}",
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[recipient],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

        # Mostrar mensaje de éxito
        messages.success(
            self.request, "¡Mensaje enviado exitosamente! Te contactaré pronto."
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        """Muestra errores cuando el formulario es inválido."""
        messages.error(self.request, "Por favor corrige los errores en el formulario.")
        return super().form_invalid(form)
