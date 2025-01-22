from django.urls import path
from .views import JobListView, JobCreateView, JobApplicationListView, JobApplicationCreateView

urlpatterns = [
    path("jobs/", JobListView.as_view(), name="job-list"),
    path("jobs/create/", JobCreateView.as_view(), name="job-create"),
    path("applications/", JobApplicationListView.as_view(), name="application-list"),
    path("applications/create/", JobApplicationCreateView.as_view(), name="application-create"),
]