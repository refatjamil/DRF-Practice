from django.shortcuts import render
from .models import Student
from . serializations import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# Create your views here.

def student(request):
    all_data = Student.objects.all()
    serialize_all_data = StudentSerializer(all_data, many=True)
    # json_all_data = JSONRenderer().render(serialize_all_data.data)
    # return HttpResponse(json_all_data, content_type='application/json')
    return JsonResponse(serialize_all_data.data, safe=False)


