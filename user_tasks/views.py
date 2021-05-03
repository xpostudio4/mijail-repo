from django.shortcuts import render

from rest_framework import viewsets

from user_tasks.models import Project
from user_tasks.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
