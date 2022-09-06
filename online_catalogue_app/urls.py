from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("login/",  login, name="login"),
    path("signup/", signup, name="signup"),
    path("signup/", choose_boss, name="choose_boss"),
    path("employee-list/", display_employee, name="display_employee"),
    path("bosses-list/", display_bosses, name="bosses_list"),
    path("sort-by-name", sort_emp_by_name, name="sort_by_name"),
    path("sort-by-doe", sort_emp_by_date_of_employment, name="sort_by_doe"),
    path("sort-by-wage", sort_by_wage, name="sort_by_wage")

]