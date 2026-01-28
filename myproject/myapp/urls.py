
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("add_employee/", views.add_employee, name="add_employee"),
    path("employee_list/", views.employee_list, name="employee_list"),
    path("employee/<int:employee_id>/", views.employee_detail, name="employee_detail"),
    path("employee/<int:employee_id>/delete/", views.employee_delete, name="employee_delete"),
    path("employee/<int:employee_id>/update/", views.employee_update, name="employee_update"),
    path("employee/<int:employee_id>/detail/", views.employee_detail, name="employee_detail"),

    ]    
