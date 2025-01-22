from rest_framework import serializers
from .models import Applicant, User, Recruiter, Company

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "is_applicant", "is_recruiter")

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "name", "description", "website", "location", "industry")


class ApplicantSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Applicant
        fields = (
            "id",
            "user",
            "phone_number",
            "resume",
            "location",
            "availability_status",
        )

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(
            username=user_data["username"],
            email=user_data["email"],
            password=user_data.get("password", None),
            is_applicant=True,
        )
        applicant = Applicant.objects.create(user=user, **validated_data)
        return applicant

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        user = instance.user

        # Update User fields
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        # Update Applicant fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

class RecruiterSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()

    class Meta:
        model = Recruiter
        fields = (
            "id",
            "user",
            "company",
            "phone_number",
        )

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        company_data = validated_data.pop("company")
        
        # Ensure the company exists or create it
        company, _ = Company.objects.get_or_create(**company_data)
        
        # Create the user for the recruiter
        user = User.objects.create_user(
            username=user_data["username"],
            email=user_data["email"],
            password=user_data.get("password", None),
            is_recruiter=True,
        )
        
        # Create the recruiter
        recruiter = Recruiter.objects.create(user=user, company=company, **validated_data)
        return recruiter

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        company_data = validated_data.pop("company", {})
        
        # Update the user fields
        user = instance.user
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()
        
        # Update or get the company
        company = instance.company
        for attr, value in company_data.items():
            setattr(company, attr, value)
        company.save()
        
        # Update recruiter fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance