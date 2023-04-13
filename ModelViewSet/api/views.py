from django.shortcuts import render
from rest_framework.response import Response
from .serializers import Student, StudentSerializer
from rest_framework import status, viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

