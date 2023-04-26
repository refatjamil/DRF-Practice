from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city', 'name']  

    # filter_backends = [SearchFilter]
    # search_fields = ['city']

    filter_backends = [OrderingFilter]
    ordering_fields = ['name']

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)

