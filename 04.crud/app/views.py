from django.shortcuts import render
import io 
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def student_api(request):

    if request.method == 'GET':
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer_data= StudentSerializer(stu)
            jason_data = JSONRenderer().render(serializer_data.data)
            return HttpResponse(jason_data, content_type='application/json')
        
        else:
            stu = Student.objects.all()
            serializer_data= StudentSerializer(stu, many=True)
            jason_data = JSONRenderer().render(serializer_data.data)
            return HttpResponse(jason_data, content_type='application/json')
        
    if request.method == 'POST':
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)
        serializer_data = StudentSerializer(data=python_data)

        if serializer_data.is_valid():
            serializer_data.save()
            res = {'msg':'Data Created'}
            jason_data = JSONRenderer().render(res)
            return HttpResponse(jason_data, content_type='application/json')

        jason_data = JSONRenderer().render(serializer_data.errors)
        return HttpResponse(jason_data, content_type='application/json')
    
    if request.method =='PUT':
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer_data = StudentSerializer(stu, data=python_data, partial= True)

        if serializer_data.is_valid():
            serializer_data.save()
            res = {'msg':'Data Updateed'}
            jason_data = JSONRenderer().render(res)
            return HttpResponse(jason_data, content_type='application/json')
        jason_data = JSONRenderer().render(serializer_data.errors)
        return HttpResponse(jason_data, content_type='application/json')
    
    
    if request.method == 'DELETE':
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'Data Deleted'}
        # jason_data = JSONRenderer().render(res)
        # return HttpResponse(jason_data, content_type='application/json')
        return JsonResponse(res, safe=False)