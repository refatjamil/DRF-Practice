from django.shortcuts import render, HttpResponse
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.

def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        print('json_data',json_data)
        stream = io.BytesIO(json_data)
        print('stream',stream)
        pythondata = JSONParser().parse(stream)
        print('pythondata',pythondata)
        id = pythondata.get('id', None)
        print('id',id)
        if id is not None:
            stu = Student.objects.get(id=id)
            print('stu',stu.q)
            serializer = StudentSerializer(stu)
            print('serializer',serializer)
            json_data = JSONRenderer().render(serializer.data)
            print('json_data',json_data)
            return HttpResponse(json_data, content_type ='application/json')
        
        else:
            stu = Student.objects.all()
            print('stu',stu)
            serializer = StudentSerializer(stu, many=True)
            print('serializer',serializer)
            json_data = JSONRenderer().render(serializer.data)
            print('json_data',json_data)
            return HttpResponse(json_data, content_type ='application/json')