from django.core.mail import send_mail
from django.views.generic import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from django.conf import settings
from django.http import JsonResponse
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
        message_text = form.cleaned_data["message"]

        # Obtener nombre del propietario del portafolio
        profile = Profile.objects.first()
        owner_name = (
            f"{profile.first_name} {profile.last_name}" if profile else "el propietario"
        )

        # Enviar email
        recipient = getattr(settings, "CONTACT_EMAIL", "email@ejemplo.com")

        send_mail(
            subject=f"[Portafolio Contacto] {subject}",
            message=f"Nuevo mensaje desde el portafolio de {owner_name}.\n\nDe: {name} <{email}>\nAsunto: {subject}\n\nMensaje:\n{message_text}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=False,
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        """Muestra errores cuando el formulario es inválido."""
        messages.error(self.request, "Por favor corrige los errores en el formulario.")
        return super().form_invalid(form)


def contact_ajax(request):
    """Vista AJAX para enviar el formulario de contacto."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data.get("subject", "Sin asunto")
            message_text = form.cleaned_data["message"]

            profile = Profile.objects.first()
            owner_name = (
                f"{profile.first_name} {profile.last_name}"
                if profile
                else "el propietario"
            )

            recipient = getattr(settings, "CONTACT_EMAIL", "email@ejemplo.com")

            send_mail(
                subject=f"[Portafolio Contacto] {subject}",
                message=f"Nuevo mensaje desde el portafolio de {owner_name}.\n\nDe: {name} <{email}>\nAsunto: {subject}\n\nMensaje:\n{message_text}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient],
                fail_silently=False,
            )

            return JsonResponse(
                {"success": True, "message": "¡Mensaje enviado exitosamente!"}
            )
        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = str(error_list[0])
            return JsonResponse({"success": False, "errors": errors}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)
