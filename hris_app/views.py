from django.shortcuts import render, get_object_or_404
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'hris_app/employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'hris_app/employee_detail.html', {'employee': employee})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'hris_app/department_list.html', {'departments': departments})

def position_list(request):
    positions = Position.objects.all()
    return render(request, 'hris_app/position_list.html', {'positions': positions})
