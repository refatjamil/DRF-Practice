from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def show_data(request):
    if request.method == 'GET':
        #----------Deserialization-----------#
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
        #----------Serialization--------------#
            student_data = Student.objects.get(id=id)
            serializer = StudentSerializer(student_data)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
        #----------Serialization--------------#
            student_data = Student.objects.all()
            serializer = StudentSerializer(student_data, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
          
        

@csrf_exempt
def create_data(request):
    if request.method == 'POST':
        json = request.body
        stream = io.BytesIO(json)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            jason_data = JSONRenderer().render(res)
            return HttpResponse(jason_data, content_type='application/json')

@csrf_exempt
def update_data(request):
    if request.method == 'PUT':
        json = request.body
        stream = io.BytesIO(json)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            jason_data = JSONRenderer().render(res)
            return HttpResponse(jason_data, content_type='application/json')


@csrf_exempt
def del_data(request):
    if request.method == 'DELETE':
        jsson_data = request.body
        stream = io.BytesIO(jsson_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student_data = Student.objects.get(id=id)
        student_data.delete()
        meg = {'meg':'Item Deleted'}
        json_data = JSONRenderer().render(meg)
        return HttpResponse(json_data, content_type='application/json')
