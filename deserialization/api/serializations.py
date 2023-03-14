from rest_framework import serializers
from .models import Student
# Create your models here.

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=70)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    