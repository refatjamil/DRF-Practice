from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dict = JSONParser().parse(stream)
        id = python_dict.get('id', None)
        if id is not None:
            student_object = Student.objects.get(id=id)
            serializer = StudentSerializer(student_object)  # student_object -->> python dict
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            all_student_object = Student.objects.all()
            serializer = StudentSerializer(all_student_object, many=True)
            return JsonResponse(serializer, safe=True)
        
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dict = JSONParser().parse(stream)
        serializer = StudentSerializer(data= python_dict)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            return JsonResponse(res, safe=True)
        
    def put(self, request, *args, **kwargs):
        json = request.body
        strm = io.BytesIO(json)
        pydict = JSONParser().parse(strm)
        id = pydict.get('id')
        stu = Student.objects.get(id=id)
        srlz = StudentSerializer(stu, data=pydict, partial=True)
        if srlz.is_valid():
            srlz.save()
            res = {'msg':'Data Updated'}
            return JsonResponse(res, safe=True)
        
    def delete(self, request, *args, **kwargs):
        json = request.body
        strm = io.BytesIO(json)
        pydict = JSONParser().parse(strm)
        id = pydict.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'Data Deleted'}
        return JsonResponse(res, safe=True)