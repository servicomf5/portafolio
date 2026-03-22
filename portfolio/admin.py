from django.contrib import admin
from .models import Profile, Skill, Experience


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "title", "email")
    fieldsets = (
        (
            "Información Personal",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "title",
                    "subtitle",
                    "bio",
                    "photo",
                    "cv",
                )
            },
        ),
        (
            "Contacto",
            {"fields": ("email", "phone", "location", "linkedin", "github", "skype")},
        ),
        ("Otros", {"fields": ("languages", "freelance_available")}),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage", "category", "order")
    list_filter = ("category",)
    list_editable = ("order", "percentage")
    ordering = ("order", "-percentage")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "type", "start_date", "end_date")
    list_filter = ("type",)
    ordering = ("-start_date",)
