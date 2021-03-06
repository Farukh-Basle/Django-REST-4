
from django.shortcuts import render
from ModelViewSet_App.models import Employee
from ModelViewSet_App.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet

class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    