from django.db import models


class Profile(models.Model):
    """Modelo singleton para la información personal del portafolio."""

    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    title = models.CharField(max_length=200, verbose_name="Título profesional")
    subtitle = models.CharField(max_length=300, blank=True, verbose_name="Subtítulo")
    bio = models.TextField(verbose_name="Biografía")
    photo = models.ImageField(upload_to="profile/", verbose_name="Foto")
    cv = models.FileField(upload_to="cv/", blank=True, null=True, verbose_name="CV")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Teléfono")
    location = models.CharField(max_length=200, verbose_name="Ubicación")
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn")
    github = models.URLField(blank=True, verbose_name="GitHub")
    skype = models.CharField(max_length=100, blank=True, verbose_name="Skype")
    languages = models.CharField(
        max_length=200, default="Español, Inglés", verbose_name="Idiomas"
    )
    freelance_available = models.BooleanField(
        default=True, verbose_name="Disponible para freelance"
    )

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfil"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        """Asegura que solo exista un perfil."""
        if not self.pk and Profile.objects.exists():
            raise ValueError("Solo puede existir un perfil. Edita el existente.")
        super().save(*args, **kwargs)


class Skill(models.Model):
    """Modelo para las habilidades técnicas y blandas."""

    CATEGORY_CHOICES = [
        ("technical", "Técnico"),
        ("soft", "Habilidades Blandas"),
        ("tools", "Herramientas"),
    ]

    name = models.CharField(max_length=100, verbose_name="Habilidad")
    percentage = models.PositiveIntegerField(default=0, verbose_name="Porcentaje")
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, verbose_name="Categoría"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")

    class Meta:
        ordering = ["order", "-percentage"]
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.name

    @property
    def category_display(self):
        """Retorna el nombre visible de la categoría."""
        return dict(self.CATEGORY_CHOICES).get(self.category, self.category)


class Experience(models.Model):
    """Modelo para experiencia laboral y educación."""

    TYPE_CHOICES = [
        ("work", "Trabajo"),
        ("education", "Educación"),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Tipo")
    title = models.CharField(max_length=200, verbose_name="Título/Puesto")
    company = models.CharField(max_length=200, verbose_name="Empresa/Institución")
    location = models.CharField(max_length=200, blank=True, verbose_name="Ubicación")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(null=True, blank=True, verbose_name="Fecha de fin")
    description = models.TextField(blank=True, verbose_name="Descripción")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")

    class Meta:
        ordering = ["-start_date"]
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"

    def __str__(self):
        return f"{self.title} en {self.company}"

    @property
    def duration(self):
        """Retorna el período formateado."""
        start = self.start_date.strftime("%b %Y")
        if self.end_date:
            end = self.end_date.strftime("%b %Y")
        else:
            end = "Presente"
        return f"{start} - {end}"
