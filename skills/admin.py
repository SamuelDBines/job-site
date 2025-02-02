from django.contrib import admin

from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)