from django import forms


class ContactForm(forms.Form):
    """Formulario de contacto."""

    name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Tu nombre", "class": "form-control"}
        ),
        label="Nombre",
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "Tu email", "class": "form-control"}
        ),
        label="Email",
    )

    subject = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Asunto (opcional)", "class": "form-control"}
        ),
        label="Asunto",
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"placeholder": "Tu mensaje", "class": "form-control", "rows": 5}
        ),
        label="Mensaje",
    )
