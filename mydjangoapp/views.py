from django.shortcuts import render
from django.http import HttpResponse

def home(request):  
    return HttpResponse("Hello, This is my Django application.")
def about(request):
    return HttpResponse("This part of the program is my about page.")
def status(request):
    return HttpResponse("This is the status page, it shows the status of the application, meaning whether it's running or not.")