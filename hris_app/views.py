from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count, Avg, Q
from .models import Employee, Department, LeaveRequest, TrainingEvent, Payroll, PerformanceReview, EmployeeDocument, Attendance, Report
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from .forms import LeaveRequestForm, EmployeeForm, DepartmentForm, EmployeeDocumentForm, TrainingEventForm, PerformanceReviewForm, PayrollForm,AttendanceForm, ReportForm

@login_required
def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to your login page

@login_required
def dashboard(request):
    context = {
        'total_employees': Employee.objects.count(),
        'active_employees': Employee.objects.filter(status='Active').count(),
        'employees_on_leave': LeaveRequest.objects.filter(status='approved', end_date__gte=timezone.now().date()).count(),
        'total_departments': Department.objects.count(),
        'recent_leave_requests': LeaveRequest.objects.order_by('-start_date')[:5],
        'upcoming_trainings' : TrainingEvent.objects.filter(start_date__gte=timezone.now()).count()
        
    }
    return render(request, 'hris_app/dashboard.html', context)

"""
@login_required
def dashboard(request):
    return render(request, 'hris_app/dashboard.html')
"""

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'hris_app/employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'hris_app/employee_detail.html', {'employee': employee})

@login_required
def employee_form(request, pk=None):
    if pk:
        employee = get_object_or_404(Employee, pk=pk)
    else:
        employee = None

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'hris_app/employee_form.html', {'form': form, 'employee': employee})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('employee_list')
    return render(request, 'hris_app/employee_confirm_delete.html', {'employee': employee})
# Add this function if it doesn't exist
@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('employee_list')
    return render(request, 'hris_app/employee_confirm_delete.html', {'employee': employee})
@login_required
def home(request):
    return render(request, 'hris_app/home.html')


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'hris_app/employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'hris_app/employee_detail.html', {'employee': employee})

@login_required
def employee_form(request, pk=None):
    if pk:
        employee = get_object_or_404(Employee, pk=pk)
    else:
        employee = None

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'hris_app/employee_form.html', {'form': form})

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'hris_app/department_list.html', {'departments': departments})

@login_required
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'hris_app/department_detail.html', {'department': department})

@login_required
def department_form(request, pk=None):
    if pk:
        department = get_object_or_404(Department, pk=pk)
    else:
        department = None

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'hris_app/department_form.html', {'form': form})

@login_required
def leave_request_list(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'hris_app/leave_request_list.html', {'leave_requests': leave_requests})

@login_required
def leave_request_detail(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    return render(request, 'hris_app/leave_request_detail.html', {'leave_request': leave_request})

@login_required
def leave_request_form(request, pk=None):
    if pk:
        leave_request = get_object_or_404(LeaveRequest, pk=pk)
    else:
        leave_request = None

    if request.method == 'POST':
        form = LeaveRequestForm(request.POST, instance=leave_request)
        if form.is_valid():
            form.save()
            return redirect('leave_request_list')
    else:
        form = LeaveRequestForm(instance=leave_request)

    return render(request, 'hris_app/leave_request_form.html', {'form': form})

@login_required
def training_list(request):
    trainings = TrainingEvent.objects.all()
    return render(request, 'hris_app/training_list.html', {'trainings': trainings})

@login_required
def training_detail(request, pk):
    training = get_object_or_404(TrainingEvent, pk=pk)
    return render(request, 'hris_app/training_detail.html', {'training': training})

@login_required
def training_form(request, pk=None):
    if pk:
        training = get_object_or_404(TrainingEvent, pk=pk)
    else:
        training = None

    if request.method == 'POST':
        form = TrainingEventForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingEventForm(instance=training)

    return render(request, 'hris_app/training_form.html', {'form': form})
@login_required
def edit_training(request, pk):
    training = get_object_or_404(TrainingEvent, pk=pk)
    if request.method == 'POST':
        form = TrainingEventForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingEventForm(instance=training)
    return render(request, 'hris_app/training_form.html', {'form': form})

@login_required
def performance_review_list(request):
    reviews = PerformanceReview.objects.all()
    return render(request, 'hris_app/performance_review_list.html', {'reviews': reviews})

@login_required
def performance_review_detail(request, pk):
    review = get_object_or_404(PerformanceReview, pk=pk)
    return render(request, 'hris_app/performance_review_detail.html', {'review': review})

@login_required
def performance_review_form(request, pk=None):
    if pk:
        review = get_object_or_404(PerformanceReview, pk=pk)
    else:
        review = None

    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('performance_review_list')
    else:
        form = PerformanceReviewForm(instance=review)

    return render(request, 'hris_app/performance_review_form.html', {'form': form})

@login_required
def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'hris_app/payroll_list.html', {'payrolls': payrolls})

@login_required
def payroll_detail(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    return render(request, 'hris_app/payroll_detail.html', {'payroll': payroll})

@login_required
def payroll_form(request, pk=None):
    if pk:
        payroll = get_object_or_404(Payroll, pk=pk)
    else:
        payroll = None

    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm(instance=payroll)

    return render(request, 'hris_app/payroll_form.html', {'form': form})

@login_required
def employee_search(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(employee_id__icontains=query)
        )
    else:
        employees = Employee.objects.all()
    return render(request, 'hris_app/employee_search.html', {'employees': employees, 'query': query})

@login_required
def department_search(request):
    query = request.GET.get('q')
    if query:
        departments = Department.objects.filter(name__icontains=query)
    else:
        departments = Department.objects.all()
    return render(request, 'hris_app/department_search.html', {'departments': departments, 'query': query})

@login_required
def training_search(request):
    query = request.GET.get('q')
    if query:
        trainings = TrainingEvent.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        )
    else:
        trainings = TrainingEvent.objects.all()
    return render(request, 'hris_app/training_search.html', {'trainings': trainings, 'query': query})

@login_required
def leave_balance(request, employee_pk):
    employee = get_object_or_404(Employee, pk=employee_pk)
    leave_balance = employee.calculate_leave_balance()
    return render(request, 'hris_app/leave_balance.html', {'employee': employee, 'leave_balance': leave_balance})

@login_required
def employee_attendance(request, employee_pk):
    employee = get_object_or_404(Employee, pk=employee_pk)
    attendance = Attendance.objects.filter(employee=employee).order_by('-date')
    return render(request, 'hris_app/employee_attendance.html', {'employee': employee, 'attendance': attendance})

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'hris_app/mark_attendance.html', {'form': form})

@login_required
def attendance_list(request):
    attendances = Attendance.objects.all().order_by('-date')
    return render(request, 'hris_app/attendance_list.html', {'attendances': attendances})

@login_required
def generate_attendance_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        attendances = Attendance.objects.filter(date__range=[start_date, end_date]).order_by('employee', 'date')
        return render(request, 'hris_app/attendance_report.html', {'attendances': attendances, 'start_date': start_date, 'end_date': end_date})
    return render(request, 'hris_app/generate_attendance_report.html')

@login_required
def employee_documents(request, employee_pk):
    employee = get_object_or_404(Employee, pk=employee_pk)
    documents = EmployeeDocument.objects.filter(employee=employee)
    return render(request, 'hris_app/employee_documents.html', {'employee': employee, 'documents': documents})

@login_required
def upload_employee_document(request, employee_pk):
    employee = get_object_or_404(Employee, pk=employee_pk)
    if request.method == 'POST':
        form = EmployeeDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.employee = employee
            document.save()
            return redirect('employee_documents', employee_pk=employee_pk)
    else:
        form = EmployeeDocumentForm()
    return render(request, 'hris_app/upload_employee_document.html', {'form': form, 'employee': employee})

@login_required
def delete_employee_document(request, document_pk):
    document = get_object_or_404(EmployeeDocument, pk=document_pk)
    employee_pk = document.employee.pk
    if request.method == 'POST':
        document.delete()
        return redirect('employee_documents', employee_pk=employee_pk)
    return render(request, 'hris_app/delete_employee_document.html', {'document': document})

@login_required
def employee_dashboard(request):
    employee = request.user.employee
    leave_requests = LeaveRequest.objects.filter(employee=employee).order_by('-start_date')[:5]
    upcoming_trainings = employee.trainings.filter(date__gte=timezone.now()).order_by('date')[:5]
    recent_payrolls = Payroll.objects.filter(employee=employee).order_by('-pay_period_end')[:3]
    recent_performance_reviews = PerformanceReview.objects.filter(employee=employee).order_by('-review_date')[:2]
    return render(request, 'hris_app/employee_dashboard.html', {
        'employee': employee,
        'leave_requests': leave_requests,
        'upcoming_trainings': upcoming_trainings,
        'recent_payrolls': recent_payrolls,
        'recent_performance_reviews': recent_performance_reviews
    })

@login_required
def hr_dashboard(request):
    pending_leave_requests = LeaveRequest.objects.filter(status='pending').count()
    upcoming_trainings = TrainingEvent.objects.filter(date__gte=timezone.now()).count()
    total_employees = Employee.objects.count()
    departments = Department.objects.annotate(employee_count=Count('employee'))
    return render(request, 'hris_app/hr_dashboard.html', {
        'pending_leave_requests': pending_leave_requests,
        'upcoming_trainings': upcoming_trainings,
        'total_employees': total_employees,
        'departments': departments
    })

@login_required
def add_participant(request, training_pk):
    training = get_object_or_404(TrainingEvent, pk=training_pk)
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        employee = get_object_or_404(Employee, pk=employee_id)
        training.participants.add(employee)
        return redirect('training_detail', pk=training_pk)
    employees = Employee.objects.exclude(trainings=training)
    return render(request, 'hris_app/add_participant_form.html', {'training': training, 'employees': employees})

@login_required
def remove_participant(request, training_pk, employee_pk):
    training = get_object_or_404(TrainingEvent, pk=training_pk)
    employee = get_object_or_404(Employee, pk=employee_pk)
    training.participants.remove(employee)
    return redirect('training_detail', pk=training_pk)

@login_required
def approve_leave_request(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    leave_request.status = 'approved'
    leave_request.save()
    return redirect('leave_request_detail', pk=pk)

@login_required
def reject_leave_request(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    leave_request.status = 'rejected'
    leave_request.save()
    return redirect('leave_request_detail', pk=pk)

@login_required
def employee_performance(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    reviews = PerformanceReview.objects.filter(employee=employee)
    return render(request, 'hris_app/employee_performance.html', {'employee': employee, 'reviews': reviews})

@login_required
def department_employees(request, pk):
    department = get_object_or_404(Department, pk=pk)
    employees = Employee.objects.filter(department=department)
    return render(request, 'hris_app/department_employees.html', {'department': department, 'employees': employees})

@login_required
def employee_trainings(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    trainings = employee.trainings.all()
    return render(request, 'hris_app/employee_trainings.html', {'employee': employee, 'trainings': trainings})

@login_required
def employee_leave_history(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    leave_requests = LeaveRequest.objects.filter(employee=employee)
    return render(request, 'hris_app/employee_leave_history.html', {'employee': employee, 'leave_requests': leave_requests})

@login_required
def employee_payroll_history(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    payrolls = Payroll.objects.filter(employee=employee)
    return render(request, 'hris_app/employee_payroll_history.html', {'employee': employee, 'payrolls': payrolls})

@login_required
def generate_payroll_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        payrolls = Payroll.objects.filter(pay_period_start__gte=start_date, pay_period_end__lte=end_date)
        return render(request, 'hris_app/payroll_report.html', {'payrolls': payrolls, 'start_date': start_date, 'end_date': end_date})
    return render(request, 'hris_app/generate_payroll_report.html')

@login_required
def generate_leave_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        leave_requests = LeaveRequest.objects.filter(start_date__gte=start_date, end_date__lte=end_date)
        return render(request, 'hris_app/leave_report.html', {'leave_requests': leave_requests, 'start_date': start_date, 'end_date': end_date})
    return render(request, 'hris_app/generate_leave_report.html')

@login_required
def generate_training_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        trainings = TrainingEvent.objects.filter(date__gte=start_date, date__lte=end_date)
        return render(request, 'hris_app/training_report.html', {'trainings': trainings, 'start_date': start_date, 'end_date': end_date})
    return render(request, 'hris_app/generate_training_report.html')

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully.')
            return redirect('employee_list')  # Assuming you have a view for listing employees
    else:
        form = EmployeeForm()
    return render(request, 'hris_app/add_employee.html', {'form': form})

@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'hris_app/edit_employee.html', {'form': form, 'employee': employee})
@login_required
def payroll_search(request):
    query = request.GET.get('q')
    if query:
        payrolls = Payroll.objects.filter(
            Q(employee__first_name__icontains=query) | 
            Q(employee__last_name__icontains=query) |
            Q(pay_period_start__icontains=query) |
            Q(pay_period_end__icontains=query)
        )
    else:
        payrolls = Payroll.objects.all()
    return render(request, 'hris_app/payroll_search.html', {'payrolls': payrolls, 'query': query})

@login_required
def recent_leave_requests(request):
    leave_requests = LeaveRequest.objects.filter(status='pending').order_by('-start_date')[:10]
    return render(request, 'hris_app/recent_leave_requests.html', {'leave_requests': leave_requests})

@login_required
def department_statistics(request):
    departments = Department.objects.annotate(
        employee_count=Count('employee'),
        avg_salary=Avg('employee__salary')
    )
    return render(request, 'hris_app/department_statistics.html', {'departments': departments})

@login_required
def employee_dashboard(request):
    employee = request.user.employee
    leave_requests = LeaveRequest.objects.filter(employee=employee).order_by('-start_date')[:5]
    upcoming_trainings = employee.trainings.filter(date__gte=timezone.now()).order_by('date')[:5]
    recent_payrolls = Payroll.objects.filter(employee=employee).order_by('-pay_period_end')[:3]
    recent_performance_reviews = PerformanceReview.objects.filter(employee=employee).order_by('-review_date')[:2]

    return render(request, 'hris_app/employee_dashboard.html', {
        'employee': employee,
        'leave_requests': leave_requests,
        'upcoming_trainings': upcoming_trainings,
        'recent_payrolls': recent_payrolls,
        'recent_performance_reviews': recent_performance_reviews
    })

@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('employee_list')
    return render(request, 'hris_app/delete_employee.html', {'employee': employee})

@login_required
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department added successfully.')
            return redirect('department_list')  # Assuming you have a department list view
    else:
        form = DepartmentForm()
    return render(request, 'hris_app/add_department.html', {'form': form})

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'hris_app/department_list.html', {'departments': departments})

@login_required
def add_leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user.employee  # Assuming the user has an associated employee
            leave_request.save()
            messages.success(request, 'Leave request submitted successfully.')
            return redirect('employee_dashboard')  # Or wherever you want to redirect after submission
    else:
        form = LeaveRequestForm()
    return render(request, 'hris_app/add_leave_request.html', {'form': form})
@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'hris_app/department_list.html', {'departments': departments})

@login_required
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department added successfully.')
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'hris_app/add_department.html', {'form': form})
@login_required
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'hris_app/department_detail.html', {'department': department})

@login_required
def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department updated successfully.')
            return redirect('department_detail', pk=pk)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'hris_app/edit_department.html', {'form': form, 'department': department})

@login_required
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        messages.success(request, 'Department deleted successfully.')
        return redirect('department_list')
    return render(request, 'hris_app/delete_department.html', {'department': department})

@login_required
def add_training(request):
    if request.method == 'POST':
        form = TrainingEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Training event added successfully.')
            return redirect('training_list')  # Assuming you have a training list view
    else:
        form = TrainingEventForm()
    return render(request, 'hris_app/add_training.html', {'form': form})
# ... rest of your view functions ...

@login_required
def delete_training(request, pk):
    training = get_object_or_404(TrainingEvent, pk=pk)
    if request.method == 'POST':
        training.delete()
        messages.success(request, 'Training event deleted successfully.')
        return redirect('training_list')
    return render(request, 'hris_app/training_confirm_delete.html', {'training': training})

@login_required
def upcoming_trainings(request):
    trainings = TrainingEvent.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'hris_app/upcoming_trainings.html', {'trainings': trainings})

@login_required
def add_payroll(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            payroll = form.save(commit=False)
            # You might want to set some fields here, e.g., created_by
            payroll.save()
            messages.success(request, 'Payroll record added successfully.')
            return redirect('payroll_list')  # Assuming you have a payroll list view
    else:
        form = PayrollForm()
    return render(request, 'hris_app/add_payroll.html', {'form': form})

@login_required
def edit_payroll(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payroll record updated successfully.')
            return redirect('payroll_list')
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'hris_app/payroll_form.html', {'form': form, 'payroll': payroll})

@login_required
def delete_payroll(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        payroll.delete()
        messages.success(request, 'Payroll record deleted successfully.')
        return redirect('payroll_list')
    return render(request, 'hris_app/payroll_confirm_delete.html', {'payroll': payroll})

@login_required
def add_performance_review(request):
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Performance review added successfully.')
            return redirect('performance_review_list')
    else:
        form = PerformanceReviewForm()
    return render(request, 'hris_app/performance_review_form.html', {'form': form})

@login_required
def edit_performance_review(request, pk):
    performance_review = get_object_or_404(PerformanceReview, pk=pk)
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST, instance=performance_review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Performance review updated successfully.')
            return redirect('performance_review_list')
    else:
        form = PerformanceReviewForm(instance=performance_review)
    return render(request, 'hris_app/performance_review_form.html', {'form': form, 'performance_review': performance_review})

@login_required
def delete_performance_review(request, pk):
    performance_review = get_object_or_404(PerformanceReview, pk=pk)
    if request.method == 'POST':
        performance_review.delete()
        messages.success(request, 'Performance review deleted successfully.')
        return redirect('performance_review_list')
    return render(request, 'hris_app/performance_review_confirm_delete.html', {'performance_review': performance_review})

@login_required
def add_employee_document(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = EmployeeDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.employee = employee
            document.save()
            messages.success(request, 'Document added successfully.')
            return redirect('employee_detail', pk=employee_id)
    else:
        form = EmployeeDocumentForm()
    return render(request, 'hris_app/add_employee_document.html', {'form': form, 'employee': employee})

@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'hris_app/employee_form.html', {'form': form, 'employee': employee})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('employee_list')
    return render(request, 'hris_app/employee_confirm_delete.html', {'employee': employee})

@login_required
def payroll_list(request):
    payrolls = Payroll.objects.all()  # Assuming you have a Payroll model
    return render(request, 'hris_app/payroll_list.html', {'payrolls': payrolls})

@login_required
def payroll_form(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm()
    return render(request, 'hris_app/payroll_form.html', {'form': form})

@login_required
def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'hris_app/payroll_list.html', {'payrolls': payrolls})

@login_required
def payroll_create(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm()
    return render(request, 'hris_app/payroll_form.html', {'form': form})

@login_required
def payroll_detail(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    return render(request, 'hris_app/payroll_detail.html', {'payroll': payroll})

@login_required
def payroll_update(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'hris_app/payroll_form.html', {'form': form})

@login_required
def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'hris_app/payroll_list.html', {'payrolls': payrolls})

@login_required
def payroll_form(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm()
    return render(request, 'hris_app/payroll_form.html', {'form': form})

@login_required
def payroll_detail(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    return render(request, 'hris_app/payroll_detail.html', {'payroll': payroll})

@login_required
def payroll_update(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'hris_app/payroll_form.html', {'form': form})

@login_required
def payroll_delete(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        payroll.delete()
        return redirect('payroll_list')
    return render(request, 'hris_app/payroll_confirm_delete.html', {'payroll': payroll})

from django.shortcuts import render, redirect
from .forms import PayrollForm  # Make sure to create this form

@login_required
def payroll_create(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm()
    return render(request, 'hris_app/payroll_form.html', {'form': form})

@login_required
def payroll_list(request):
    payrolls = Payroll.objects.all()  # Make sure to import the Payroll model
    return render(request, 'hris_app/payroll_list.html', {'payrolls': payrolls})

@login_required
def report_list(request):
    # This is a placeholder. You'll need to customize this based on what kind of reports you want to show.
    reports = []  # You might want to fetch actual report data here
    return render(request, 'hris_app/report_list.html', {'reports': reports})

@login_required
def document_list(request):
    documents = EmployeeDocument.objects.all()
    return render(request, 'hris_app/document_list.html', {'documents': documents})


@login_required
def document_form(request):
    if request.method == 'POST':
        form = EmployeeDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Document added successfully.')
            return redirect('document_list')
    else:
        form = EmployeeDocumentForm()
    return render(request, 'hris_app/document_form.html', {'form': form})

@login_required
def edit_document(request, pk):
    document = get_object_or_404(EmployeeDocument, pk=pk)
    if request.method == 'POST':
        form = EmployeeDocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            messages.success(request, 'Document updated successfully.')
            return redirect('document_list')
    else:
        form = EmployeeDocumentForm(instance=document)
    return render(request, 'hris_app/document_form.html', {'form': form, 'document': document})

@login_required
def delete_document(request, pk):
    document = get_object_or_404(EmployeeDocument, pk=pk)
    if request.method == 'POST':
        document.delete()
        messages.success(request, 'Document deleted successfully.')
        return redirect('document_list')
    return render(request, 'hris_app/document_confirm_delete.html', {'document': document})
    
@login_required
def report_form(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.created_by = request.user
            report.save()
            messages.success(request, 'Report created successfully.')
            return redirect('report_list')  # Assuming you have a report list view
    else:
        form = ReportForm()
    return render(request, 'hris_app/report_form.html', {'form': form})

@login_required
def delete_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        report.delete()
        messages.success(request, 'Report deleted successfully.')
        return redirect('report_list')  # Assuming you have a report list view
    return render(request, 'hris_app/report_confirm_delete.html', {'report': report})

@login_required
def edit_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            messages.success(request, 'Report updated successfully.')
            return redirect('report_list')  # Assuming you have a report list view
    else:
        form = ReportForm(instance=report)
    return render(request, 'hris_app/report_form.html', {'form': form, 'report': report})


@login_required
def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'hris_app/department_form.html', {'form': form, 'department': department})

@login_required
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'hris_app/department_confirm_delete.html', {'department': department})

def payroll_update(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('payroll_detail', pk=payroll.pk)
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'hris_app/payroll_update.html', {'form': form, 'payroll': payroll})


