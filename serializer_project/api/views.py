from django.shortcuts import render
from .models import Student
from . serializations import StuentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.


def student(request):
    stu = Student.objects.all()
    serializer = StuentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data, safe=False)
