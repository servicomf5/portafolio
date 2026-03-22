from django.db import models
from django.urls import reverse


class Project(models.Model):
    """Modelo para los proyectos del portafolio."""

    TYPE_CHOICES = [
        ("bootcamp", "Bootcamp"),
        ("private", "Privado"),
    ]

    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, verbose_name="URL slug")
    description = models.TextField(verbose_name="Descripción")
    project_type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, verbose_name="Tipo"
    )
    technologies = models.CharField(max_length=500, verbose_name="Tecnologías")
    demo_url = models.URLField(blank=True, verbose_name="URL Demo")
    repo_url = models.URLField(blank=True, verbose_name="URL Repositorio")
    image = models.ImageField(upload_to="projects/", verbose_name="Imagen")
    featured = models.BooleanField(default=False, verbose_name="Destacado")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")

    class Meta:
        ordering = ["order", "-pk"]
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})


class CaseStudy(models.Model):
    """Modelo para el caso de estudio del bootcamp."""

    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción breve")
    challenge = models.TextField(verbose_name="Desafío principal")
    solution = models.TextField(verbose_name="Solución propuesta")
    tools = models.TextField(verbose_name="Herramientas utilizadas")
    metrics = models.TextField(
        verbose_name="Métricas de impacto", help_text="Una métrica por línea"
    )
    learnings = models.TextField(verbose_name="Principales aprendizajes")
    technical_skills = models.TextField(verbose_name="Habilidades técnicas aplicadas")
    justification = models.TextField(verbose_name="Justificación")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")

    class Meta:
        ordering = ["order"]
        verbose_name = "Caso de Estudio"
        verbose_name_plural = "Casos de Estudio"

    def __str__(self):
        return self.title
