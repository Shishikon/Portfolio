from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import SkillSerializer, ProjectsSerializer, AboutSerializer, CertificationsSerializer, EducationSerializer
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
    skills = Skill.objects.all()
    projects = Project.objects.all()
    about = About.objects.all()
    certifications = Certification.objects.all()
    education = Education.objects.all()

    context = {
        "skills": skills,
        "projects": projects,
        "about": about,
        "certifications": certifications,
        "education": education
    }




    return render(request, 'index.html', context)