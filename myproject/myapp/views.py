from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return  render(request,"home.html")
def html2(request):
    return  render(request,"html2.html")
    