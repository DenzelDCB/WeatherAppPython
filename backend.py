import requests
import pandas as pd
from datetime import datetime

BASE_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODE_MAP = {
    0: "Sunny (Clear sky)",
    1: "Sunny (Mostly clear)",
    2: "Partly cloudy",
    3: "Cloudy sky",
    45: "Foggy weather",
    48: "Less foggy",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Heavy drizzle",
    56: "Freezing Drizzle: Light",
    57: "Freezing Drizzle: Dense",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Freezing Rain: Light",
    67: "Freezing Rain: Heavy",
    71: "Light snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Little snow",
    80: "Light rain showers",
    81: "Moderate rain showers",
    82: "Heavy rain showers",
    85: "Snow showers slight",
    86: "Snow showers heavy",
    95: "Mild thunderstorm",
    96: "Thunderstorm with light hail",
    99: "Thunderstorm with heavy hail"
}

def getHourlyWeather():
    try:
        LAT = 6.4183
        LON = 2.88132

        params = {
            "latitude": LAT,
            "longitude": LON,
            "hourly": "temperature_2m,weathercode",
            "timezone": "auto",
            "forecast_days": 15,  
            "past_days": 1,
            "temperature_unit": "fahrenheit"
        }

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        model = response.json()

        if "hourly" not in model or "temperature_2m" not in model["hourly"] or "weathercode" not in model["hourly"]:
            return "Error: Missing 'hourly' data in the model."

        hourly_forecast = model["hourly"]
        times = hourly_forecast["time"]
        temperatures = hourly_forecast["temperature_2m"]
        weather_codes = hourly_forecast["weathercode"]

        current_date = datetime.now().strftime("%Y-%m-%d")

        today_data = []
        future_data = []
        for i in range(len(times)):
            date, hour = times[i].split("T")
            weather = WEATHER_CODE_MAP.get(weather_codes[i], "Unknown")
            temp = temperatures[i]
            if date == current_date:
                today_data.append([date, hour, weather, f"{temp}°F"])
            else:
                future_data.append([date, hour, weather, f"{temp}°F"])

        today_df = pd.DataFrame(today_data, columns=["Date", "Hour", "Weather", "Temperature"])
        future_df = pd.DataFrame(future_data, columns=["Date", "Hour", "Weather", "Temperature"])

        return "Today\n\n" + today_df.to_string(index=False) + "\n\nNext 15 days\n\n" + future_df.to_string(index=False)
    except Exception as e:
        return f"An error occurred: {e}"
