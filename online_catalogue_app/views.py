from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from . import forms
from django_seed import Seed
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'online_catalogue_app/html/base.html')


def seed_db(request):
    seeder = Seed.seeder()
    seeder.add_seeder()


def display_employee(request, page=1):
    query_results = EmployeeModel.objects.all()

    context = {
        "query_results": query_results,
    }

    return render(request, 'online_catalogue_app/html/employee.html', context)


def display_employee_full_info(request):
    query_results = EmployeeModel.objects.all()
    context = {
        "query_results": query_results
    }

    return render(request, 'online_catalogue_app/html/employee_detail.html', context)


def display_bosses(request):
    query_results = BossModel.objects.all()

    context = {
        "query_results": query_results
    }

    return render(request, 'online_catalogue_app/html/bosses.html', context)


def login_employee(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username, password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:display_employee")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()

    context = {
        "form": form
    }

    return render(request, 'online_catalogue_app/html/login.html', context)


def register_employee(request):
    if request.method == "POST":
        form = forms.NewEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            login(request, employee)
            messages.success(request, "Registration successful.")
            return redirect("main:display_employee")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = forms.NewEmployeeForm()

    context = {
        "register_form": form
    }

    return render(request, 'online_catalogue_app/html/signup.html', context)


def sort_emp_by_name(request):
    sorted_names = EmployeeModel.objects.order_by("emp_full_name")
    context = {
        "sorted_names": sorted_names
    }

    return render(request, 'online_catalogue_app/html/sort_by_name.html', context)


def sort_emp_by_name_reverse(request):
    sorted_names = EmployeeModel.objects.order_by("emp_full_name").reverse()
    context = {
        "sorted_names": sorted_names
    }

    return render(request, 'online_catalogue_app/html/sort_by_name_reverse.html', context)


def sort_emp_by_position(request):
    employees = EmployeeModel.objects.all()
    order = ['intern', 'junior', 'middle', 'senior', 'team-lead']
    order = {key: i for i, key in enumerate(order)}
    ordered_positions = sorted(employees, key=lambda employee: order.get(employee.position, 0))


def sort_emp_by_date_of_employment(request):
    sorted_list = EmployeeModel.objects.order_by("date_of_employment")
    context = {
        "sorted_list": sorted_list
    }

    return render(request, 'online_catalogue_app/html/sort_by_doe.html', context)


def sort_emp_by_date_of_employment_reverse(request):
    sorted_list = EmployeeModel.objects.order_by("date_of_employment").reverse()
    context = {
        "sorted_list": sorted_list
    }

    return render(request, 'online_catalogue_app/html/sort_by_doe_reverse.html', context)


def sort_by_wage(request):
    sorted_list = EmployeeModel.objects.order_by("wage")
    context = {
        "sorted_list": sorted_list
    }

    return render(request, 'online_catalogue_app/html/sort_by_wage.html', context)


def sort_by_wage_reverse(request):
    sorted_list = EmployeeModel.objects.order_by("wage").reverse()
    context = {
        "sorted_list": sorted_list
    }

    return render(request, 'online_catalogue_app/html/sort_by_wage_reverse.html', context)


def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get("search")
        if query == "":
            return redirect('employee-list/')
        results = EmployeeModel.objects.filter(Q(emp_full_name__contains=query) |
                                               Q(position__contains=query) |
                                               Q(boss_name__boss_full_name__contains=query))

    context = {
        'query': query,
        'results': results
    }

    return render(request, 'online_catalogue_app/html/search.html', context)
