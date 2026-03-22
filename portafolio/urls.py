"""
URL configuration for portafolio project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
    path("projects/", include("projects.urls")),
    path("content/", include("content.urls")),
    path("contact/", include("contact.urls")),
]

# Serve media and static in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom error handlers
handler404 = "portafolio.views.handler404"
handler500 = "portafolio.views.handler500"
