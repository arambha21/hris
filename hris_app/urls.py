from django.urls import path
from .views import EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/new/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]