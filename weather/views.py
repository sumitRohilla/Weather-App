from django.shortcuts import render
from django.conf import settings
import urllib.request
import json


# Create your views here.


def index(request):

    if request.method == "POST":
        city = request.POST["place"]
        city1 = "+".join(city.split(" "))

        api_key = settings.WEATHER_API_KEY

        print(api_key)

        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city1}&appid={api_key}"
        )
        res = urllib.request.urlopen(url).read()

        json_date = json.loads(res)
        print(json_date)
        data = {
            "country_code": str(json_date["sys"]["country"]),
            "coordinate": f'{str(json_date["coord"]["lon"])} {str(json_date["coord"]["lat"])}',
            "temp": f'{str(round(json_date["main"]["temp"] - 273.15, 2))} °C',
            "weather": str(json_date["weather"][0]["description"]),
            "pressure": str(json_date["main"]["pressure"]),
            "humidity": str(json_date["main"]["humidity"]),
        }
    else:
        city = ""
        data = {}
    return render(request, "index.html", {"city": city, "data": data})
