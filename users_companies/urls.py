from django.urls import path
from . import views

urlpatterns = [
    # Applicant views
    path("applicants/", views.ApplicantListCreateView.as_view(), name="applicant-list"),
    path("applicants/<int:pk>/", views.ApplicantDetailView.as_view(), name="applicant-detail"),

    # Company URLs
    path("companies/", views.CompanyListCreateView.as_view(), name="company-list"),
    path("companies/<int:pk>/", views.CompanyDetailView.as_view(), name="company-detail"),

    # Recruiter URLs
    path("recruiters/", views.RecruiterListCreateView.as_view(), name="recruiter-list"),
    path("recruiters/<int:pk>/", views.RecruiterDetailView.as_view(), name="recruiter-detail"),
]

# urlpatterns = [
    # path("register/", views.RegisterUserView.as_view(), name="register"),
    # path("login/", views.LoginView.as_view(), name="login"),
    # path("profile/", views.UserProfileView.as_view(), name="profile"),
# ]