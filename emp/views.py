from django.shortcuts import render
from emp.models import Employee
from django.shortcuts import render, redirect
from django.http import JsonResponse
from emp.forms import EmployeeForm
from rest_framework import viewsets
from .serializer import *


def emp(request):
     if request.method=='POST':
         form=EmployeeForm(request.POST)
         if form.is_valid():
             try:
                 form.save()
                 return redirect('/show/')
             except:
                 pass
     else:
         form=EmployeeForm()
     return render(request,'index.html',{'form':form})

# class Empviewset(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = Empserializer
#     return JsonResponse({"empdata":serializer_class.data})


def show(request):
    empoyees = Employee.objects.all
    return render(request, 'show.html', {'employees': empoyees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')
