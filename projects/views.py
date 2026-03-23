from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Project, CaseStudy
from portfolio.models import Profile


class PortfolioView(TemplateView):
    """Vista para la página de portfolio."""

    template_name = "portfolio/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        context["projects"] = Project.objects.all()
        context["case_study"] = CaseStudy.objects.first()
        return context
