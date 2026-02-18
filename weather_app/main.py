from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import parse_weather
from weather_app.weather_display import display_weather


def main():
    city = input("Enter city name: ")

    api = WeatherAPI()

    try:
        raw_data = api.get_current_weather(city)
        weather = parse_weather(raw_data)
        display_weather(weather)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()