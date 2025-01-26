from django.urls import path
from . import views

app_name = 'hris_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('departments/', views.department_list, name='department_list'),
    path('positions/', views.position_list, name='position_list'),
]