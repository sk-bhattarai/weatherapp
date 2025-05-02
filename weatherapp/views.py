from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
from .models import WeatherSearch

def index(request):
    API_KEY = '1759247bd0be8e875e795f249b7d8aee'  # Your API key
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric"

    if request.method == "POST":
        city1 = request.POST.get('city1', '').strip()
        city2 = request.POST.get('city2', '').strip()

        if not city1:
            messages.error(request, "Please enter at least one city")
            return render(request, "weatherapp/index.html")

        try:
            weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_url)
            # Save the search to database
            WeatherSearch.objects.create(
                city=city1,
                temperature=weather_data1['temperature'],
                description=weather_data1['description'],
                humidity=weather_data1['humidity'],
                wind_speed=weather_data1['wind_speed'],
                pressure=weather_data1['pressure']
            )
        except Exception as e:
            messages.error(request, f"Error fetching weather for {city1}: {str(e)}")
            weather_data1, daily_forecasts1 = None, None

        weather_data2, daily_forecasts2 = None, None
        if city2:
            try:
                weather_data2, daily_forecasts2 = fetch_weather_and_forecast(city2, API_KEY, current_weather_url, forecast_url)
                # Save the search to database
                WeatherSearch.objects.create(
                    city=city2,
                    temperature=weather_data2['temperature'],
                    description=weather_data2['description'],
                    humidity=weather_data2['humidity'],
                    wind_speed=weather_data2['wind_speed'],
                    pressure=weather_data2['pressure']
                )
            except Exception as e:
                messages.error(request, f"Error fetching weather for {city2}: {str(e)}")

        context = {
            "weather_data1": weather_data1,
            "daily_forecasts1": daily_forecasts1,
            "weather_data2": weather_data2,
            "daily_forecasts2": daily_forecasts2,
        }
        
        return render(request, "weatherapp/index.html", context)
    else:
        return render(request, "weatherapp/index.html")

def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    # Fetch current weather
    response = requests.get(current_weather_url.format(city, api_key))
    response.raise_for_status()
    weather_data = response.json()
    
    # Prepare current weather data
    weather_info = {
        "city": city,
        "temperature": round(weather_data['main']['temp'], 2),
        "description": weather_data['weather'][0]['description'].capitalize(),
        "icon": weather_data['weather'][0]['icon'],
        "humidity": weather_data['main']['humidity'],
        "wind_speed": weather_data['wind']['speed'],
        "pressure": weather_data['main']['pressure']
    }

    # Fetch 5-day forecast
    forecast_response = requests.get(forecast_url.format(city, api_key))
    forecast_response.raise_for_status()
    forecast_data = forecast_response.json()
    
    # Process forecast data
    daily_forecasts = []
    # Create a dictionary to store daily data (we'll take the middle reading of each day)
    daily_data = {}
    
    for item in forecast_data['list']:
        # Convert timestamp to date object
        date = datetime.datetime.fromtimestamp(item['dt'])
        date_str = date.strftime('%Y-%m-%d')
        
        # If we don't have this date yet, or if this is a mid-day reading (around 12:00)
        if date_str not in daily_data or (12 <= date.hour <= 14):
            daily_data[date_str] = {
                "day": date.strftime("%A"),
                "min_temp": item['main']['temp_min'],
                "max_temp": item['main']['temp_max'],
                "description": item['weather'][0]['description'].capitalize(),
                "icon": item['weather'][0]['icon'],
                "humidity": item['main']['humidity'],
                "wind_speed": item['wind']['speed']
            }
    
    # Convert daily_data dictionary to a list of the first 5 days
    daily_forecasts = list(daily_data.values())[:4]
    
    return weather_info, daily_forecasts





