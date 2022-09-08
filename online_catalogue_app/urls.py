from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("login/",  login_employee, name="login"),
    path("signup/", register_employee, name="signup"),
    path("logout/", logout_employee, name="logout"),
    path("employee-list/", display_employee, name="display_employee"),
    path("employee-list-full-info/", display_employee_full_info, name="display_employee_full_info"),
    path("bosses-list/", display_bosses, name="bosses_list"),
    path("sort-by-name/", sort_emp_by_name, name="sort_by_name"),
    path("sort-by-name-reverse-order/", sort_emp_by_name_reverse, name="sort_by_name_reverse_order"),
    path("sort-by-doe/", sort_emp_by_date_of_employment, name="sort_by_doe"),
    path("sort-by-doe-reverse_order/", sort_emp_by_date_of_employment_reverse, name="sort_by_doe_reverse_order"),
    path("sort-by-wage/", sort_by_wage, name="sort_by_wage"),
    path("sort-by-wage-reverse-order/", sort_by_wage_reverse, name="sort_by_wage_reverse_order"),
    path("search/", search, name="search")
]