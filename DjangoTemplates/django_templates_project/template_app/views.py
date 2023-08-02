from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return render(request, "template_app/first.html")

def weather_view(request):
    weather_dictionary = {
        "Istanbul" : "30", 
        "Amsterdam" : "20",
        "Paris" : [5,14,20,21],
        "Rome" : {"morning" : 10, "evening" : 20},
        "user_premium" : True,
        "test" : "Test test Test test"
        }
    return render(request,"template_app/weather.html", context=weather_dictionary)