from django.shortcuts import render
from django.http import HttpResponse

# create view ==> add to urls.py here, then in parent class.
def home(request):
    return HttpResponse('HOME PAGE \n Welcome to our capstone website')
