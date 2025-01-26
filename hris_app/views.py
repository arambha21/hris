from django.shortcuts import render
from .models import Employee, Department

def home(request):
    return render(request, 'hris_app/home.html')

def employee_list(request):
    employees = Employee.objects.all().select_related('position__department')
    return render(request, 'hris_app/employee_list.html', {'employees': employees})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'hris_app/department_list.html', {'departments': departments})
