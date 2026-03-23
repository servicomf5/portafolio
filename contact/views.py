from django.core.mail import send_mail
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

        # Construir el cuerpo del email
        email_body = f"""
Mensaje desde el portafolio de {owner_name}.

De: {name} <{email}>

{message}
"""

        # Enviar email al destino configurado
        recipient = getattr(settings, "CONTACT_EMAIL", "email@ejemplo.com")
        send_mail(
            subject=f"[Portafolio Contacto] {subject}",
            message=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
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
