from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Pull Data from DB
    # Transform Data
    # Send Email
    # request -> response
    # request handler
    # action
    return render(request, './main/index.html')


# Create your views here
