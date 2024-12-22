from django.shortcuts import render

from .models import Employee

# Create your views here.


def home(request):

    employee=Employee.objects.all()

    context = {
        'employee':employee
    }
    return render(request,'home.html',context)


def __str__(self):

    return f' {self.ename}' 