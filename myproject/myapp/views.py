
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django import forms
from .models import Employee,User,Employee_Leave
from django.contrib.auth.hashers import make_password
from .form import EmployeeForm,EmployeeUpdateForm,Leave_Form

from django.shortcuts import get_object_or_404

# Create your views here.


#===========================Admin dashboard view=====================================
def home(request):
    return  render(request,"home.html")
# view to add a new employee
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
          
            user = User.objects.create(
                username=form.cleaned_data['username'],
                password=make_password(form.cleaned_data['password']),
                role=form.cleaned_data['role']
            )

         
            employee = form.save(commit=False)
            employee.user = user
            employee.save()

            return redirect('employee_list')

    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})


# view to list all employees
def employee_list(request):
    status_filter = request.GET.get('status', 'all')
    
    if status_filter == 'enabled':
        employees = Employee.objects.filter(status='Enabled')
    elif status_filter == 'disabled':
        employees = Employee.objects.filter(status='Disabled')
    else:
        employees = Employee.objects.all()
    
    return render(request, 'employee_list.html', {
        'employees': employees,
        'status_filter': status_filter
    })

#view to show employee details
def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'employee_details.html', {'employee': employee})

# view to delete employee
def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if employee.user:
        employee.user.delete()
    employee.delete()
    return redirect('employee_list')

# view to update employee details
def employee_update(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == "POST":
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', employee_id=employee.id)
        

    else:
        form = EmployeeUpdateForm(instance=employee)

    return render(request, 'update_employee.html', {
        'form': form,
        'employee': employee
    })
#Leave application views
def leave_applications(request):
    status = request.GET.get('status', 'all')
    leaves = Employee_Leave.objects.all()
    if status in ['Approved', 'Rejected', 'Pending']:
        leaves = leaves.filter(Leave_Status=status)

    return render(request, 'leave_applications.html', {
        'leaves': leaves,
        'status': status,
    })
#view to update leave status
def status_update(request, leave_id, new_status):
    leave = get_object_or_404(Employee_Leave, id=leave_id)
    leave.Leave_Status = new_status
    leave.save()
    return redirect('leave_applications')

#================================login page view===============================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        login(request,user)
        if user and user.check_password(password) and user.role == 'Admin':
          
            return redirect('home')
        elif user and user.check_password(password) and user.role == 'Employee' and user.employee.status == 'Enabled':
            return redirect('employee_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials or inactive account.'})
    return render(request, 'login.html')

#logout view
def logout_view(request):
    logout(request)
    return redirect('login')


#========================employee views========================#

#employee dashboard view
def employee_dashboard(request):
    return render(request, 'employee/employee.html')
#user profile view    
def user_profile(request):
    employee = request.user.employee
    return render(request, 'employee/user_profile.html', {'employee': employee})

#view to apply leave
def apply_leave(request):
    if request.method == "POST":
        form = Leave_Form(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            total_leave_days = (leave.leave_end_date - leave.leave_start_date).days+1 
            if leave.Leave_type == 'half-day':
                total_leave_days -= 0.5
                
            leave.employee = request.user.employee
            leave.Leave_count = total_leave_days
            leave.save()
            return redirect('leave_history')
    else:
        form = Leave_Form()
    
    return render(request, 'employee/apply_leave.html', {'form': form})

#view to see leave history
def leave_history(request):
    employee = request.user.employee
    status = request.GET.get('status', 'all')
    leaves = Employee_Leave.objects.filter(employee=employee)
    if status in ['Approved', 'Rejected', 'Pending']:
        leaves = leaves.filter(Leave_Status=status)

    return render(request, 'employee/leave_history.html', {
        'leaves': leaves,
        'status': status,
    })

