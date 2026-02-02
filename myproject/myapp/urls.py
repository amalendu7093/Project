
from django.urls import path,include
from . import views

urlpatterns = [
    path("admin/",views.home,name="home"),
    path("add_employee/", views.add_employee, name="add_employee"),
    path("employee_list/", views.employee_list, name="employee_list"),
    path("employee/<int:employee_id>/", views.employee_detail, name="employee_detail"),
    path("employee/<int:employee_id>/delete/", views.employee_delete, name="employee_delete"),
    path("employee/<int:employee_id>/update/", views.employee_update, name="employee_update"),
    path("employee/<int:employee_id>/detail/", views.employee_detail, name="employee_detail"),
    path("leave_applications/", views.leave_applications, name="leave_applications"),
    path("status_update/<int:leave_id>/<str:new_status>/", views.status_update, name="status_update"),
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    #employee leave urls
    path("employee/dashboard/", views.employee_dashboard, name="employee_dashboard"),
    path("employee/leave/", views.apply_leave, name="apply_leave"),
    path("employee/leave/history/", views.leave_history, name="leave_history"),
    path("employee/userprofile/", views.user_profile, name="user_profile"),
    

    ]    
