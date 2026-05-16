from django.urls import path
from .views import *
from .tests import *

urlpatterns = [
    path('', home, name='index'),

]
