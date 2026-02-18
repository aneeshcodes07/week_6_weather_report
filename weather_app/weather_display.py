def display_weather(weather):
    print("\n===== Weather Report =====")
    print(f"City: {weather['city']}")
    print(f"Temperature: {weather['temperature']} °C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Pressure: {weather['pressure']} hPa")
    print(f"Condition: {weather['description']}")
    print(f"Wind Speed: {weather['wind_speed']} m/s")
    print("==========================\n")