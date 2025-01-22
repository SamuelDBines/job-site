from rest_framework import serializers
from .models import Job, JobApplication
from skills.models import Skill
from skills.serializers import SkillSerializer
from users_companies.models import Company, Recruiter, Applicant
from users_companies.serializers import CompanySerializer, RecruiterSerializer

class JobSerializer(serializers.ModelSerializer):
    skills_required = SkillSerializer(many=True, read_only=True)  # Nested skills
    company = CompanySerializer(read_only=True)  # Nested company
    recruiter = RecruiterSerializer(read_only=True)  # Nested recruiter

    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "description",
            "skills_required",
            "company",
            "recruiter",
            "location",
            "employment_type",
            "salary_min",
            "salary_max",
            "posted_at",
            "expires_at",
            "is_active",
        ]
    
class WritableJobSerializer(serializers.ModelSerializer):
    skills_required = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Skill.objects.all()
    )
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    recruiter = serializers.PrimaryKeyRelatedField(queryset=Recruiter.objects.all())

    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "description",
            "skills_required",
            "company",
            "recruiter",
            "location",
            "employment_type",
            "salary_min",
            "salary_max",
            "posted_at",
            "expires_at",
            "is_active",
        ]


class JobApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)  # Nested job
    applicant = serializers.StringRelatedField(read_only=True)  # Display applicant's username
    reviewed_by = serializers.StringRelatedField(read_only=True)  # Display reviewer's username

    class Meta:
        model = JobApplication
        fields = [
            "id",
            "job",
            "applicant",
            "status",
            "applied_at",
            "reviewed_by",
            "comments",
        ]

class WritableJobApplicationSerializer(serializers.ModelSerializer):
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())
    applicant = serializers.PrimaryKeyRelatedField(queryset=Applicant.objects.all())
    reviewed_by = serializers.PrimaryKeyRelatedField(
        queryset=Recruiter.objects.all(), required=False
    )

    class Meta:
        model = JobApplication
        fields = [
            "id",
            "job",
            "applicant",
            "status",
            "applied_at",
            "reviewed_by",
            "comments",
        ]