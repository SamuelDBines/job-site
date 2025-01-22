from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_applicant = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="applicant_profile")
    skills = models.ManyToManyField("skills.Skill", related_name="applicants", blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    availability_status = models.CharField(
        max_length=50,
        choices=[
            ("Actively Looking", "Actively Looking"),
            ("Open to Offers", "Open to Offers"),
            ("Not Looking", "Not Looking"),
        ],
        default="Open to Offers",
    )

    def __str__(self):
        return f"Applicant: {self.user.username}"
    
class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="recruiter_profile")
    company = models.ForeignKey("Company", on_delete=models.CASCADE, related_name="recruiters")
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Recruiter: {self.user.username} ({self.company.name})"
    
class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name