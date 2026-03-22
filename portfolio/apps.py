from django.apps import AppConfig
from django.contrib import admin


class PortfolioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portfolio"
    verbose_name = "Portfolio"

    def ready(self):
        """Configure admin after Django is ready."""
        admin.site.site_header = "Portafolio Admin"
        admin.site.site_title = "Portafolio"
        admin.site.index_title = "Gestión de Contenido"
