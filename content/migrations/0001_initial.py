from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FodaMatrix",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fortalezas",
                    models.TextField(
                        help_text="Una fortaleza por línea", verbose_name="Fortalezas"
                    ),
                ),
                (
                    "debilidades",
                    models.TextField(
                        help_text="Una debilidad por línea", verbose_name="Debilidades"
                    ),
                ),
                (
                    "oportunidades",
                    models.TextField(
                        help_text="Una oportunidad por línea",
                        verbose_name="Oportunidades",
                    ),
                ),
                (
                    "amenazas",
                    models.TextField(
                        help_text="Una amenaza por línea", verbose_name="Amenazas"
                    ),
                ),
            ],
            options={
                "verbose_name": "Matriz FODA",
                "verbose_name_plural": "Matriz FODA",
            },
        ),
        migrations.CreateModel(
            name="CompanyResearch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "company_name",
                    models.CharField(
                        max_length=200, verbose_name="Nombre de la empresa"
                    ),
                ),
                ("company_url", models.URLField(verbose_name="URL de la empresa")),
                (
                    "technical_values",
                    models.TextField(
                        help_text="Un valor por línea", verbose_name="Valores técnicos"
                    ),
                ),
                ("products", models.TextField(verbose_name="Productos/Servicios")),
                (
                    "technologies",
                    models.TextField(
                        help_text="Una tecnología por línea", verbose_name="Tecnologías"
                    ),
                ),
                (
                    "methodologies",
                    models.TextField(verbose_name="Metodologías de trabajo"),
                ),
                ("innovation", models.TextField(verbose_name="Enfoque de innovación")),
                (
                    "contribution_ways",
                    models.TextField(
                        help_text="Una forma por línea",
                        verbose_name="Formas de aportar",
                    ),
                ),
                (
                    "interview_questions",
                    models.TextField(
                        help_text="Una pregunta por línea",
                        verbose_name="Preguntas para entrevista",
                    ),
                ),
            ],
            options={
                "verbose_name": "Investigación de Empresa",
                "verbose_name_plural": "Investigación de Empresas",
            },
        ),
    ]
