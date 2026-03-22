from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Profile, Skill, Experience
from projects.models import Project, CaseStudy
from content.models import FodaMatrix, CompanyResearch


class HomeView(TemplateView):
    """Vista para la página de inicio (hero)."""

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        context["featured_projects"] = Project.objects.filter(featured=True)[:3]
        return context


class AboutView(TemplateView):
    """Vista para la página About."""

    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        context["skills"] = Skill.objects.all()
        context["experiences"] = Experience.objects.all()
        context["foda"] = FodaMatrix.objects.first()
        context["company"] = CompanyResearch.objects.first()
        return context
