from django.shortcuts import render
from rest_framework import generics

from api.v1.serializers import TechStackSerializer, ProjectsSerializer, AboutSerializer, CertificationsSerializer, EducationSerializer
from .models import TechStack, Project, About, Certification, Education


def home(request):
    return render(request, 'home.html')

class TechStackListApi(generics.ListAPIView):
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer

class ProjectListApi(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer

class AboutListApi(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class CertificationListApi(generics.ListAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationsSerializer

class EducationListApi(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


