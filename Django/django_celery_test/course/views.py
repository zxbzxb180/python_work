from django.shortcuts import render
from course.tasks import CourseTask
from django.http import JsonResponse

# Create your views here.


def do(request):
    print('start do request')
    CourseTask.delay()
    print('end do request')

    return JsonResponse({'result': 'ok'})