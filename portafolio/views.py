"""
Custom error handlers for portafolio project.
"""

from django.http import HttpResponseNotFound, HttpResponseServerError
from django.template import loader


def handler404(request, exception):
    """Custom 404 error page."""
    template = loader.get_template("404.html")
    return HttpResponseNotFound(template.render())


def handler500(request):
    """Custom 500 error page."""
    template = loader.get_template("500.html")
    return HttpResponseServerError(template.render())
