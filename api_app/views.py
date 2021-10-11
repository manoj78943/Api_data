from django.contrib import messages
from django.shortcuts import render
import requests
def ok(request):
    return render(request,"api.html")

def deaths(request) :
    major = requests.get('https://api.covid19api.com/dayone/country/india').json()
    messages.success(request, " COVID API is fetching data-- Number of deaths with respect to date.")
    return render(request, "deaths.html", {'record': major,})

def recovered(request) :
    major = requests.get('https://api.covid19api.com/dayone/country/india').json()
    messages.success(request, "COVID API is fetching data-- Number of recovered patients with respect to date.")
    return render(request, "recovered.html", {'record': major,})

def active(request):
    major = requests.get('https://api.covid19api.com/dayone/country/india').json()
    messages.success(request, "COVID API is fetching data-- Number of active patients with respect to date.")
    return render(request, "active.html", {'record': major,})