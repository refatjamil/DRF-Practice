from django.shortcuts import render, HttpResponse
import io
from rest_framework.parsers import JSONParser
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .models import Student
# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondate = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondate)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')
        
    else:
        all_data = Student.objects.all()
        serializer = StudentSerializer(all_data, many=True)
        json = JSONRenderer().render(serializer.data)
        return HttpResponse(json, content_type='application/json')    