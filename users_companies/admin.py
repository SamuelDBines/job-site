from django.contrib import admin

from .models import User, Applicant, Recruiter, Company

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_applicant", "is_recruiter")

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number", "availability_status")

@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ("user", "company", "phone_number")

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "website", "industry")