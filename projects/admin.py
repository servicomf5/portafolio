from django.contrib import admin
from .models import Project, CaseStudy


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "project_type", "featured", "order")
    list_filter = ("project_type", "featured")
    list_editable = ("order", "featured")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order", "-pk")


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    ordering = ("order",)
