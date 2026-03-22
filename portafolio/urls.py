"""
URL configuration for portafolio project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
    path("projects/", include("projects.urls")),
    path("content/", include("content.urls")),
    path("contact/", include("contact.urls")),
]

# Serve media files in production (always enabled for uploads)
urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

# Serve static in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom error handlers
handler404 = "portafolio.views.handler404"
handler500 = "portafolio.views.handler500"
