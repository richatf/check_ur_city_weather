from django.shortcuts import render
import urllib.request
import json
import re
from datetime import datetime

# Create your views here.

def home(request):

    if request.method == 'POST':
        city = request.POST['city']
        # retrieving information from weather api
        source = urllib.request.urlopen('api.openweathermap.org/data/2.5/forecast?q='+city+'&appid=79cfece3ef7fd9bbb613824b625add2b')

        # json file

        list_of_data = json.loads(source)
        data = {
            'country_code': str(list_of_data['sys']['country']),
            'cor': str(list_of_data["coord"]["lon"]) + " " + str(list_of_data["coord"]["lat"]),
            'temp': str(list_of_data["main"]["temp"]),
            'pressure': str(list_of_data["main"]["pressure"]),
            'humidity': str(list_of_data["main"]["humidity"]),
            'main': str(list_of_data["weather"][0]['description']),
            'icon': list_of_data["weather"][0]['icon'],
            'city': city
        }

        #responses = response.json
        #print(responses)

        #print("Selected City is :" + city)
        #print("Current weather :" + str(data['main']['temp'] - 273) + "F"
    else:
        data = {}

    return render(request, 'home.html', data)
