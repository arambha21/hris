from django.contrib import admin
from .models import Department, Position, Employee, LeaveRequest, TrainingEvent, PerformanceReview, Payroll, Attendance, EmployeeDocument

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(LeaveRequest)
admin.site.register(TrainingEvent)
admin.site.register(PerformanceReview)
admin.site.register(Payroll)
admin.site.register(Attendance)
admin.site.register(EmployeeDocument)