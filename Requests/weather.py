import requests
import json

def get_weather(city):
    api_key = "ac7f2a3e37c365f5926e1843bde13f47"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def display_weather(data):
    if data["cod"] == 200:
        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        print("Weather: ", weather)
        print("Description: ", description)
        print("Temperature: ", temp, "K")
        print("Feels Like: ", feels_like, "K")
        print("Humidity: ", humidity, "%")
        print("Wind Speed: ", wind_speed, "m/s")
    else:
        print("Error retrieving weather data. Ensure you typed in the city name correctly.")

def validate_city(city):
    if city.isalpha():
        return True
    else:
        print("Invalid city name. City name should only contain alphabets.")
        return False

def get_city_input():
    while True:
        city = input("Enter a city name: ")
        if validate_city(city):
            return city

def main():
    city = get_city_input()
    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
