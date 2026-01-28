from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from .models import Employee,User
from django.contrib.auth.hashers import make_password
from .form import EmployeeForm

from django.shortcuts import get_object_or_404

# Create your views here.
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
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

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
        employee.name = request.POST.get('name')
        employee.department = request.POST.get('department')
        employee.email = request.POST.get('email')
        employee.phone_number = request.POST.get('phone_number')
     
        employee.status = request.POST.get('status')

        employee.save()
        return redirect('employee_list')  

    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'update_employee.html', {
        'form': form,
        'employee': employee
    })
