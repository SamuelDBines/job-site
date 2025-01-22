from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Job, JobApplication
from .serializers import JobSerializer, WritableJobSerializer, JobApplicationSerializer, WritableJobApplicationSerializer

class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobCreateView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = WritableJobSerializer

class JobApplicationListView(ListAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class JobApplicationCreateView(CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = WritableJobApplicationSerializer