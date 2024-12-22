from django.shortcuts import render

# Create your views here.


def home(request):

    employee = Employee.objects.all()