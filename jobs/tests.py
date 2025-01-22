from django.test import TestCase
from users_companies.models import Company, Recruiter, Applicant
from skills.models import Skill
from jobs.models import Job, JobApplication

# class JobModelTestCase(TestCase):
#     def setUp(self):
#         # Create a Company
#         self.company = Company.objects.create(
#             name="TechCorp",
#             description="A leading tech company."
#         )

#         # Create a Recruiter
#         self.recruiter = Recruiter.objects.create(
#             user=None,  # Add a User instance if needed
#             company=self.company
#         )

#         # Create an Applicant
#         self.applicant = Applicant.objects.create(
#             user=None  # Add a User instance if needed
#         )

#         # Create Skills
#         self.skill_python = Skill.objects.create(name="Python")
#         self.skill_django = Skill.objects.create(name="Django")

#         # Create a Job
#         self.job = Job.objects.create(
#             title="Backend Developer",
#             description="Looking for a skilled backend developer.",
#             company=self.company,
#             recruiter=self.recruiter,
#             location="Remote",
#             employment_type="Full-Time",
#             salary_min=60000,
#             salary_max=90000,
#             is_active=True
#         )
#         self.job.skills_required.set([self.skill_python, self.skill_django])

#     def test_job_creation(self):
#         """Test that the job is created successfully with the correct fields."""
#         job = self.job
#         self.assertEqual(job.title, "Backend Developer")
#         self.assertEqual(job.company, self.company)
#         self.assertEqual(job.recruiter, self.recruiter)
#         self.assertIn(self.skill_python, job.skills_required.all())
#         self.assertIn(self.skill_django, job.skills_required.all())

#     def test_job_application_creation(self):
#         """Test that a job application can be created and linked to a job and an applicant."""
#         application = JobApplication.objects.create(
#             job=self.job,
#             applicant=self.applicant,
#             status="Submitted",
#             comments="Excited to apply for this position."
#         )
#         self.assertEqual(application.job, self.job)
#         self.assertEqual(application.applicant, self.applicant)
#         self.assertEqual(application.status, "Submitted")
#         self.assertEqual(application.comments, "Excited to apply for this position.")

#     def test_job_application_unique_together_constraint(self):
#         """Test that the unique_together constraint prevents duplicate applications."""
#         # Create the first application
#         JobApplication.objects.create(
#             job=self.job,
#             applicant=self.applicant,
#             status="Submitted"
#         )

#         # Try creating a duplicate application
#         with self.assertRaises(Exception):
#             JobApplication.objects.create(
#                 job=self.job,
#                 applicant=self.applicant,
#                 status="In Review"
#             )

#     def test_job_active_status(self):
#         """Test that the job's active status can be toggled."""
#         self.assertTrue(self.job.is_active)  # Initially active
#         self.job.is_active = False
#         self.job.save()
#         self.assertFalse(self.job.is_active)  # Deactivated
