from django.db import models


class FodaMatrix(models.Model):
    """Modelo singleton para la matriz FODA."""

    fortalezas = models.TextField(
        verbose_name="Fortalezas", help_text="Una fortaleza por línea"
    )
    debilidades = models.TextField(
        verbose_name="Debilidades", help_text="Una debilidad por línea"
    )
    oportunidades = models.TextField(
        verbose_name="Oportunidades", help_text="Una oportunidad por línea"
    )
    amenazas = models.TextField(
        verbose_name="Amenazas", help_text="Una amenaza por línea"
    )

    class Meta:
        verbose_name = "Matriz FODA"
        verbose_name_plural = "Matriz FODA"

    def __str__(self):
        return "Matriz FODA"

    def save(self, *args, **kwargs):
        """Asegura que solo exista una matriz FODA."""
        if not self.pk and FodaMatrix.objects.exists():
            raise ValueError("Solo puede existir una matriz FODA. Edita la existente.")
        super().save(*args, **kwargs)

    def get_fortalezas_list(self):
        return [f.strip() for f in self.fortalezas.split("\n") if f.strip()]

    def get_debilidades_list(self):
        return [d.strip() for d in self.debilidades.split("\n") if d.strip()]

    def get_oportunidades_list(self):
        return [o.strip() for o in self.oportunidades.split("\n") if o.strip()]

    def get_amenazas_list(self):
        return [a.strip() for a in self.amenazas.split("\n") if a.strip()]


class CompanyResearch(models.Model):
    """Modelo para la investigación de empresa objetivo."""

    company_name = models.CharField(max_length=200, verbose_name="Nombre de la empresa")
    company_url = models.URLField(verbose_name="URL de la empresa")
    technical_values = models.TextField(
        verbose_name="Valores técnicos", help_text="Un valor por línea"
    )
    products = models.TextField(verbose_name="Productos/Servicios")
    technologies = models.TextField(
        verbose_name="Tecnologías", help_text="Una tecnología por línea"
    )
    methodologies = models.TextField(verbose_name="Metodologías de trabajo")
    innovation = models.TextField(verbose_name="Enfoque de innovación")
    contribution_ways = models.TextField(
        verbose_name="Formas de aportar", help_text="Una forma por línea"
    )
    interview_questions = models.TextField(
        verbose_name="Preguntas para entrevista", help_text="Una pregunta por línea"
    )

    class Meta:
        verbose_name = "Investigación de Empresa"
        verbose_name_plural = "Investigación de Empresas"

    def __str__(self):
        return self.company_name

    def get_technical_values_list(self):
        return [v.strip() for v in self.technical_values.split("\n") if v.strip()]

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split("\n") if t.strip()]

    def get_contribution_ways_list(self):
        return [c.strip() for c in self.contribution_ways.split("\n") if c.strip()]

    def get_interview_questions_list(self):
        return [q.strip() for q in self.interview_questions.split("\n") if q.strip()]
