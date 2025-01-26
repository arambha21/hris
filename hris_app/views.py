from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee
from .forms import EmployeeForm

class EmployeeListView(ListView):
    model = Employee
    template_name = 'hris_app/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'hris_app/employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'hris_app/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'hris_app/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'hris_app/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')
