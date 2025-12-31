from django.shortcuts import render
from .models import SearchHistory
import requests
# Create your views here.
api_key = "9b1513440c37070f2a2b70ddbeeea552"


def index(request):
    weather =None
    error =None
    recent_searches = SearchHistory.objects.order_by('-searched_at')[:5]
    if request.method == "POST":
        city = request.POST.get('city','').strip()
        if city:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            try:
                response = requests.get(url,timeout=5)
                data=response.json()
                if response.status_code == 200:
                    weather={
                        'city': f"{data['name']}, {data['sys']['country']}",
                        'temperature': data['main']['temp'],
                        'humidity': data['main']['humidity'],
                        'pressure': data['main']['pressure'],
                        'description': data['weather'][0]['description'].title(),
                        'icon': data['weather'][0]['icon'],
                    }
                    SearchHistory.objects.create(
                        city_name=data['name'],
                        temperature=data['main']['temp'],
                        humidity=data['main']['humidity'],
                        pressure=data['main']['pressure'],
                        description=data['weather'][0]['description'].title())
                    recent_searches = SearchHistory.objects.order_by('-searched_at')[:5]
                else:
                    error=data.get('message','Could not retrieve data')
            except requests.RequestException:
                error="Network error, please try again."
        else:
            error='please enter a city name'

    return render(request,'index.html',{
        'weather':weather,
        'error':error,
        'recent_searches':recent_searches
    })
