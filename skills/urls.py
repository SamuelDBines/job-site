from django.urls import path
from . import views

urlpatterns = [
    path("skills/", views.SkillListCreateView.as_view(), name="skill-list"),
    path("skills/<int:pk>/", views.SkillDetailView.as_view(), name="skill-detail"),
]