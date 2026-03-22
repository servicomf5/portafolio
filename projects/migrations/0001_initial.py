from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=200, verbose_name="Título")),
                ("slug", models.SlugField(unique=True, verbose_name="Slug")),
                ("description", models.TextField(verbose_name="Descripción")),
                (
                    "project_type",
                    models.CharField(
                        choices=[("bootcamp", "Bootcamp"), ("private", "Privado")],
                        default="private",
                        max_length=20,
                        verbose_name="Tipo",
                    ),
                ),
                (
                    "technologies",
                    models.CharField(max_length=500, verbose_name="Tecnologías"),
                ),
                ("demo_url", models.URLField(blank=True, verbose_name="URL Demo")),
                (
                    "repo_url",
                    models.URLField(blank=True, verbose_name="URL Repositorio"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="projects/",
                        verbose_name="Imagen",
                    ),
                ),
                (
                    "featured",
                    models.BooleanField(default=False, verbose_name="Destacado"),
                ),
                ("order", models.PositiveIntegerField(default=0, verbose_name="Orden")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Proyecto",
                "verbose_name_plural": "Proyectos",
                "ordering": ["order", "-pk"],
            },
        ),
        migrations.CreateModel(
            name="CaseStudy",
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
                ("title", models.CharField(max_length=200, verbose_name="Título")),
                ("description", models.TextField(verbose_name="Descripción breve")),
                ("challenge", models.TextField(verbose_name="Desafío principal")),
                ("solution", models.TextField(verbose_name="Solución propuesta")),
                ("tools", models.TextField(verbose_name="Herramientas utilizadas")),
                (
                    "metrics",
                    models.TextField(
                        help_text="Una métrica por línea",
                        verbose_name="Métricas de impacto",
                    ),
                ),
                (
                    "learnings",
                    models.TextField(verbose_name="Principales aprendizajes"),
                ),
                (
                    "technical_skills",
                    models.TextField(verbose_name="Habilidades técnicas aplicadas"),
                ),
                ("justification", models.TextField(verbose_name="Justificación")),
                ("order", models.PositiveIntegerField(default=0, verbose_name="Orden")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Caso de Estudio",
                "verbose_name_plural": "Casos de Estudio",
                "ordering": ["order"],
            },
        ),
    ]
