from django.shortcuts import render
from rest_framework import viewsets

from api.models import Projects
from api.serializers import ProjectsSerializer


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
