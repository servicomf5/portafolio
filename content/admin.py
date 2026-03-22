from django.contrib import admin
from .models import FodaMatrix, CompanyResearch


@admin.register(FodaMatrix)
class FodaMatrixAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(CompanyResearch)
class CompanyResearchAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_url")
