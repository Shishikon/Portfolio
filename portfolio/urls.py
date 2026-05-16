from django.urls import path
from .views import *
from .tests import *

urlpatterns = [
    path('', home, name='index'),

    path('api/v1/skills/', SkillListApi.as_view()),
    path('api/v1/projects/', ProjectListApi.as_view()),
    path('api/v1/about/', AboutListApi.as_view()),
    path('api/v1/certifications/', CertificationListApi.as_view()),
    path('api/v1/education/', EducationListApi.as_view()),
]
