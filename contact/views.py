from django.core.mail import send_mail
from django.views.generic import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ContactForm


class ContactView(FormView):
    """Vista para el formulario de contacto."""

    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        """Envía el email cuando el formulario es válido."""
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        subject = form.cleaned_data.get("subject", "Sin asunto")
        message = form.cleaned_data["message"]

        # Construir el cuerpo del email
        email_body = f"""
Mensaje desde el portafolio de Eduardo Muñoz.

De: {name} <{email}>

{message}
"""

        # Enviar email
        send_mail(
            subject=f"[Portafolio Contacto] {subject}",
            message=email_body,
            from_email=None,  # Usa DEFAULT_FROM_EMAIL
            recipient_list=["eduardomunoz.trabajo@gmail.com"],
            fail_silently=False,
        )

        # Mostrar mensaje de éxito
        messages.success(
            self.request, "¡Mensaje enviado exitosamente! Te contactaré pronto."
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        """Muestra errores cuando el formulario es inválido."""
        messages.error(self.request, "Por favor corrige los errores en el formulario.")
        return super().form_invalid(form)
