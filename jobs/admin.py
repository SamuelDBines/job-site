from django.contrib import admin

from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "recruiter", "location", "is_active", "posted_at", "expires_at")
    list_filter = ("company", "is_active", "employment_type", "posted_at")
    search_fields = ("title", "description", "company__name")

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("job", "applicant", "status", "applied_at", "reviewed_by")
    list_filter = ("status", "applied_at")
    search_fields = ("job__title", "applicant__user__username")
