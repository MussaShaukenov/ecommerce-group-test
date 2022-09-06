from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'online_catalogue_app/html/base.html')


def display_employee(request):
    query_results = EmployeeModel.objects.all()
    context = {
        "query_results": query_results
    }

    return render(request, 'online_catalogue_app/html/employee.html', context)


def display_bosses(request):
    query_results = BossModel.objects.all()

    context = {
        "query_results": query_results
    }

    return render(request, 'online_catalogue_app/html/bosses.html', context)


def login(request):
    return render(request, 'online_catalogue_app/html/login.html', None)


def signup(request):
    return render(request, 'online_catalogue_app/html/signup.html', None)


def choose_boss(request):
    query_results = EmployeeModel.objects.values_list('boss_full_name')
    context = {
        "query_results": query_results
    }

    return render(request, 'online_catalogue_app/html/signup.html', context)


def sort_emp_by_name(request):
    sorted_names = EmployeeModel.objects.order_by("emp_full_name")
    context = {
        "sorted_names": sorted_names
    }

    return render(request, 'online_catalogue_app/html/sort_by_name.html', context)


def sort_emp_by_date_of_employment(request):
    sorted_list = EmployeeModel.objects.order_by("date_of_employment")
    context = {
        "sorted_list":  sorted_list
    }

    return render(request, 'online_catalogue_app/html/sort_by_doe.html', context)


def sort_by_wage(request):
    sorted_list = EmployeeModel.objects.order_by("wage")
    context = {
        "sorted_list": sorted_list
    }

    return render(request, 'online_catalogue_app/html/sort_by_wage.html', context)
