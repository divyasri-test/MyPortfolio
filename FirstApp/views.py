from django.shortcuts import render
from django.http import HttpResponse

# create a function
def home(response):
    return render(response, "FirstApp/home.html", {})

def index(response):
    return render(response, "FirstApp/index.html", {})
