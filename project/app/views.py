from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def home(request):
    data= Student.objects.filter(Name='mehak patel').update(Name='mihu')
    # data1=data.values()
    print(data)
    return HttpResponse(data)

