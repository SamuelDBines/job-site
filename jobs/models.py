from django.db import models
from users_companies.models import Recruiter, Company, Applicant
from skills.models import Skill

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills_required = models.ManyToManyField("skills.Skill", related_name="jobs", blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name="jobs")
    location = models.CharField(max_length=255)
    employment_type = models.CharField(
        max_length=50,
        choices=[
            ("Full-Time", "Full-Time"),
            ("Part-Time", "Part-Time"),
            ("Contract", "Contract"),
            ("Internship", "Internship"),
        ],
        default="Full-Time",
    )
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    skills_required = models.ManyToManyField(Skill, related_name="jobs", blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="applications")
    status = models.CharField(
        max_length=50,
        choices=[
            ("Submitted", "Submitted"),
            ("In Review", "In Review"),
            ("Shortlisted", "Shortlisted"),
            ("Rejected", "Rejected"),
            ("Hired", "Hired"),
        ],
        default="Submitted",
    )
    applied_at = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(Recruiter, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("job", "applicant")

    def __str__(self):
        return f"{self.applicant.user.username} applied for {self.job.title}"