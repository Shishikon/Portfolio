from django.urls import path
from .views import *
from .tests import *

urlpatterns = [
    path('', home, name='index'),

    path('api/v1/skills/', SkillListApi.as_view(), name="skills"),
    path('api/v1/projects/', ProjectListApi.as_view(), name="projects"),
    path('api/v1/about/', AboutListApi.as_view(), name="about"),
    path('api/v1/certifications/', CertificationListApi.as_view(), name="certifications"),
    path('api/v1/education/', EducationListApi.as_view(), name="education"),
]
