from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import EmployeeModel
from django.contrib.auth.models import User


class NewEmployeeForm(UserCreationForm):
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = EmployeeModel
        fields = ("emp_full_name", "position", "date_of_employment", "wage", "boss_name", "password1", "password2")

    def save(self, commit=True):
        employee = super(NewEmployeeForm, self).save(commit=False)
        employee.password1 = self.cleaned_data['password1']
        employee.password2 = self.cleaned_data['password2']
        if commit:
            employee.save()
        return employee
