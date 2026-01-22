
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("html2",views.html2,name="html2")

   
]
