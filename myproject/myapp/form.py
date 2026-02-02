from django import forms
from .models import Employee,User,Employee_Leave
class EmployeeForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True)
    status = forms.ChoiceField(choices=[('Enabled', 'Enabled'), ('Disabled', 'Disabled')], required=True)

    class Meta:
        model = Employee
        fields = ['name', 'department', 'join_date', 'phone_number', 'email', 'status']
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date'}),
        }

class EmployeeUpdateForm(forms.ModelForm):
    status = forms.ChoiceField(choices=[('Enabled', 'Enabled'), ('Disabled', 'Disabled')], required=True)

    class Meta:
        model = Employee
        fields = ['name', 'department', 'phone_number', 'email', 'status']

class Leave_Form(forms.ModelForm):
    class Meta:
        model = Employee_Leave
        fields = ['leave_start_date','leave_end_date', 'reason']
        widgets = {
            'leave_start_date': forms.DateInput(attrs={'type': 'date'}),
            'leave_end_date': forms.DateInput(attrs={'type': 'date'}),

        }