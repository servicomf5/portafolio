from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("first_name", models.CharField(max_length=100, verbose_name="Nombre")),
                (
                    "last_name",
                    models.CharField(max_length=100, verbose_name="Apellido"),
                ),
                (
                    "title",
                    models.CharField(max_length=200, verbose_name="Título profesional"),
                ),
                (
                    "subtitle",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Subtítulo"
                    ),
                ),
                ("bio", models.TextField(verbose_name="Biografía")),
                ("photo", models.ImageField(upload_to="profile/", verbose_name="Foto")),
                (
                    "cv",
                    models.FileField(
                        blank=True, null=True, upload_to="cv/", verbose_name="CV"
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Teléfono"
                    ),
                ),
                (
                    "location",
                    models.CharField(max_length=200, verbose_name="Ubicación"),
                ),
                ("linkedin", models.URLField(blank=True, verbose_name="LinkedIn")),
                ("github", models.URLField(blank=True, verbose_name="GitHub")),
                (
                    "skype",
                    models.CharField(blank=True, max_length=100, verbose_name="Skype"),
                ),
                (
                    "languages",
                    models.CharField(
                        default="Español, Inglés",
                        max_length=200,
                        verbose_name="Idiomas",
                    ),
                ),
                (
                    "freelance_available",
                    models.BooleanField(
                        default=True, verbose_name="Disponible para freelance"
                    ),
                ),
            ],
            options={
                "verbose_name": "Perfil",
                "verbose_name_plural": "Perfil",
            },
        ),
        migrations.CreateModel(
            name="Skill",
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
                ("name", models.CharField(max_length=100, verbose_name="Habilidad")),
                (
                    "percentage",
                    models.PositiveIntegerField(default=0, verbose_name="Porcentaje"),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("technical", "Técnico"),
                            ("soft", "Habilidades Blandas"),
                            ("tools", "Herramientas"),
                        ],
                        max_length=20,
                        verbose_name="Categoría",
                    ),
                ),
                ("order", models.PositiveIntegerField(default=0, verbose_name="Orden")),
            ],
            options={
                "verbose_name": "Habilidad",
                "verbose_name_plural": "Habilidades",
                "ordering": ["order", "-percentage"],
            },
        ),
        migrations.CreateModel(
            name="Experience",
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
                    "type",
                    models.CharField(
                        choices=[("work", "Trabajo"), ("education", "Educación")],
                        max_length=20,
                        verbose_name="Tipo",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=200, verbose_name="Título/Puesto"),
                ),
                (
                    "company",
                    models.CharField(
                        max_length=200, verbose_name="Empresa/Institución"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="Ubicación"
                    ),
                ),
                ("start_date", models.DateField(verbose_name="Fecha de inicio")),
                (
                    "end_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de fin"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Descripción"),
                ),
                ("order", models.PositiveIntegerField(default=0, verbose_name="Orden")),
            ],
            options={
                "verbose_name": "Experiencia",
                "verbose_name_plural": "Experiencias",
                "ordering": ["-start_date"],
            },
        ),
    ]
