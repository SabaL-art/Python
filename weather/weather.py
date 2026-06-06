import requests
import sys
from config import API_KEY  # config file contains api key


def get_weather(city):
    api_key = API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        print("Error: ", data.get("message"))
        sys.exit()

    return data


def main():
    city = input("Enter city name:")
    weather_data = get_weather(city.strip())
    weather = weather_data["weather"][0]["main"]
    humidity = weather_data["main"]["humidity"]
    temp = weather_data["main"]["temp"]
    city_name = weather_data["name"]
    country = weather_data["sys"]["country"]
    print("City:", city_name)
    print("Country:", country)
    print("weather= ", weather)
    print("humidity= ", humidity, "%")
    print("temperature =", temp, "°C")


if __name__ == "__main__":
    main()
