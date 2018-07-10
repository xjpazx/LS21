from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Robot
from .serializers import RobotModelSerializer


class RobotModelViewSet(ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotModelSerializer
