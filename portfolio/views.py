from django.shortcuts import render
from rest_framework import generics

from api.v1.serializers import SkillSerializer, ProjectsSerializer, AboutSerializer, CertificationsSerializer, EducationSerializer
from .models import Skill, Project, About, Certification, Education



class SkillListApi(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

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


def home(request):
    return render(request, 'index.html')