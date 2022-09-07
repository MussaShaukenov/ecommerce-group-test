from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import EmployeeModel


class NewEmployeeForm(UserCreationForm):
    class Meta:
        model = EmployeeModel
        fields = ("emp_full_name", "position", "date_of_employment", "wage", "boss_name")

    def save(self, commit=True):
        employee = super(NewEmployeeForm, self).save(commit=False)
        if commit:
            employee.save()
        return employee
