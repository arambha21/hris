from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'hris_app/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_employees'] = Employee.objects.count()
        return context

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'hris_app/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'hris_app/employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'hris_app/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'hris_app/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'hris_app/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')
