from rest_framework import serializers
from .models import Skill, Project, About, Certification, Education


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class CertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
