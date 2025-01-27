from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='positions')

    def __str__(self):
        return self.title

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    hire_date = models.DateField()
    birth_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    annual_leave_days = models.PositiveIntegerField(default=20)
    STATUS_CHOICES = [
        ('probation', 'Probation'),
        ('permanent', 'Permanent'),
        ('contract', 'Contract'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='probation')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def calculate_leave_balance(self):
        current_year = timezone.now().year
        total_leave = self.annual_leave_days
        used_leave = LeaveRequest.objects.filter(
            employee=self,
            start_date__year=current_year,
            status='approved'
        ).aggregate(models.Sum('duration'))['duration__sum'] or 0
        return total_leave - used_leave

    def update_status(self):
        today = timezone.now().date()
        if self.hire_date:
            tenure = relativedelta(today, self.hire_date)
            if tenure.years >= 1 and self.status == 'probation':
                self.status = 'permanent'
                self.save()

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    LEAVE_TYPES = [
        ('annual', 'Annual Leave'),
        ('sick', 'Sick Leave'),
        ('personal', 'Personal Leave'),
    ]
        # Add more leave types as needed
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField(default=1)
    reason = models.TextField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.employee} - {self.start_date} to {self.end_date}"

# Add other models (TrainingEvent, PerformanceReview, Payroll, Attendance, EmployeeDocument) here

class TrainingEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    duration = models.DurationField()
    location = models.CharField(max_length=200)
    trainer = models.CharField(max_length=100)
    participants = models.ManyToManyField(Employee, related_name='trainings')

    def __str__(self):
        return self.title

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviews_given')
    review_date = models.DateField()
    performance_score = models.DecimalField(max_digits=3, decimal_places=2)
    comments = models.TextField()

    def __str__(self):
        return f"{self.employee} - {self.review_date}"

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employee} - {self.pay_period_start} to {self.pay_period_end}"

    def calculate_net_pay(self):
        self.net_pay = self.base_salary + self.overtime_pay - self.deductions
        self.save()

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.employee} - {self.date}"

class EmployeeDocument(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100)
    file = models.FileField(upload_to='employee_documents/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.document_type}"