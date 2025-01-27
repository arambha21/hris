from django.urls import path
from django.contrib.auth.models import User

# List all users
all_users = User.objects.all()
for user in all_users:
    print(f"Username: {user.username}, Email: {user.email}, Is superuser: {user.is_superuser}")

# List only superusers
superusers = User.objects.filter(is_superuser=True)
for user in superusers:
    print(f"Superuser - Username: {user.username}, Email: {user.email}")
from . import views

urlpatterns = [
    # Employee related URLs
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/<int:pk>/edit/', views.edit_employee, name='edit_employee'),
    path('employees/<int:pk>/delete/', views.delete_employee, name='delete_employee'),
    path('employees/<int:pk>/performance/', views.employee_performance, name='employee_performance'),
    path('employees/<int:pk>/trainings/', views.employee_trainings, name='employee_trainings'),
    path('employees/<int:pk>/leave-history/', views.employee_leave_history, name='employee_leave_history'),
    path('employees/<int:pk>/payroll-history/', views.employee_payroll_history, name='employee_payroll_history'),
    path('employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),

    # Department related URLs
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('departments/<int:pk>/edit/', views.edit_department, name='edit_department'),
    path('departments/<int:pk>/delete/', views.delete_department, name='delete_department'),
    path('departments/<int:pk>/employees/', views.department_employees, name='department_employees'),
    path('department-statistics/', views.department_statistics, name='department_statistics'),

    # Leave request related URLs
    path('leave-requests/', views.leave_request_list, name='leave_request_list'),
    path('leave-requests/add/', views.add_leave_request, name='add_leave_request'),
    path('leave-requests/<int:pk>/', views.leave_request_detail, name='leave_request_detail'),
    path('leave-requests/<int:pk>/approve/', views.approve_leave_request, name='approve_leave_request'),
    path('leave-requests/<int:pk>/reject/', views.reject_leave_request, name='reject_leave_request'),
    path('recent-leave-requests/', views.recent_leave_requests, name='recent_leave_requests'),

    # Training related URLs
    path('trainings/', views.training_list, name='training_list'),
    path('trainings/add/', views.add_training, name='add_training'),
    path('trainings/<int:pk>/', views.training_detail, name='training_detail'),
    path('trainings/<int:pk>/edit/', views.edit_training, name='edit_training'),
    path('trainings/<int:pk>/delete/', views.delete_training, name='delete_training'),
    path('trainings/<int:training_pk>/add-participant/', views.add_participant, name='add_participant'),
    path('trainings/<int:training_pk>/remove-participant/<int:employee_pk>/', views.remove_participant, name='remove_participant'),
    path('upcoming-trainings/', views.upcoming_trainings, name='upcoming_trainings'),

    # Payroll related URLs
    path('payrolls/', views.payroll_list, name='payroll_list'),
    path('payrolls/add/', views.add_payroll, name='add_payroll'),
    path('payrolls/<int:pk>/', views.payroll_detail, name='payroll_detail'),
    path('payrolls/<int:pk>/edit/', views.edit_payroll, name='edit_payroll'),
    path('payrolls/<int:pk>/delete/', views.delete_payroll, name='delete_payroll'),
    path('payroll-search/', views.payroll_search, name='payroll_search'),

    # Performance review related URLs
    path('performance-reviews/', views.performance_review_list, name='performance_review_list'),
    path('performance-reviews/add/', views.add_performance_review, name='add_performance_review'),
    path('performance-reviews/<int:pk>/', views.performance_review_detail, name='performance_review_detail'),
    path('performance-reviews/<int:pk>/edit/', views.edit_performance_review, name='edit_performance_review'),
    path('performance-reviews/<int:pk>/delete/', views.delete_performance_review, name='delete_performance_review'),

    # Document related URLs
    path('employees/<int:employee_pk>/documents/', views.employee_documents, name='employee_documents'),
    path('employees/<int:employee_pk>/documents/add/', views.add_employee_document, name='add_employee_document'),
    path('documents/<int:document_pk>/delete/', views.delete_employee_document, name='delete_employee_document'),

    # Report related URLs
    path('reports/payroll/', views.generate_payroll_report, name='generate_payroll_report'),
    path('reports/leave/', views.generate_leave_report, name='generate_leave_report'),
    path('reports/training/', views.generate_training_report, name='generate_training_report'),

    # Dashboard URLs
    path('dashboard/', views.dashboard, name='dashboard'),

    # Other URLs
    path('home/', views.home, name='home'),
]