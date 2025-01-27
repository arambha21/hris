from django import forms
from .models import Employee, Department, LeaveRequest, TrainingEvent, PerformanceReview, Payroll, Attendance, EmployeeDocument, Report

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'department', 'email','phone_number', ]

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'leave_type', 'reason']

class TrainingEventForm(forms.ModelForm):
    class Meta:
        model = TrainingEvent
        fields = ['title', 'description', 'date', 'duration', 'location', 'trainer', 'participants']

class PerformanceReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview
        fields = ['employee', 'review_date', 'reviewer', 'performance_score', 'comments']

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee', 'pay_period_start', 'pay_period_end', 'base_salary', 'overtime_pay', 'deductions', 'net_pay']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'time_in', 'time_out']

class EmployeeDocumentForm(forms.ModelForm):
    class Meta:
        model = EmployeeDocument
        fields = ['employee', 'document_type', 'file']

from django import forms
from .models import Report  # Assuming you have a Report model

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description', 'report_type']  # Adjust fields as per your Report model