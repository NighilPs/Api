from django.shortcuts import render
from django . http import HttpResponse
from . models import server
import requests

# Create your views here.

def data(request):
    response=requests.get("https://22a7bc24-975b-4bda-8515-f0ad2fa8d0d1.mock.pstmn.io/dummy").json()
    for i in response:
        value = server(test=response['data'])
        value.save()
    return HttpResponse("data saved")

