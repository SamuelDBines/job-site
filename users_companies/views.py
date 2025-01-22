from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Applicant, Recruiter, Company
from .serializers import ApplicantSerializer, RecruiterSerializer, CompanySerializer

# List all applicants or create a new applicant
class ApplicantListCreateView(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]  # Anyone can create an applicant
        return [IsAuthenticated()]  # Authentication required for listing applicants


# Retrieve, update, or delete a specific applicant
class ApplicantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = [IsAuthenticated]

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]  # Anyone can create a company
        return [IsAuthenticated()]  # Authentication required for listing companies


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

# Recruiter Views
class RecruiterListCreateView(generics.ListCreateAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]  # Anyone can create a recruiter
        return [IsAuthenticated()]  # Authentication required for listing recruiters


class RecruiterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    permission_classes = [IsAuthenticated]