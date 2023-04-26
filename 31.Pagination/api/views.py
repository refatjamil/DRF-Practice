from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .paginations import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination

# class StudentList(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     pagination_class = MyPageNumberPagination

# class StudentList(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     pagination_class = MyLimitOffsetPagination    

class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination 