from django.shortcuts import render , redirect
from django.http import HttpResponse

from .utils import send_email_to_client

# Create your views here.

def send_email(request):
    send_email_to_client()
    return redirect('/')

def first(request):
    return render(request , 'index.html')