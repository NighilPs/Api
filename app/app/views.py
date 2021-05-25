from django.shortcuts import render
from django . http import HttpResponse
from . models import server
import requests

# Create your views here.

def data(request):
    data = request.POST['data']
    value = server(test=data)
    value.save()
    return HttpResponse("data saved")

