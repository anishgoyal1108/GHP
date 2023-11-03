import requests
import json

def compare_weather(city1, city2):
    api_key = "ac7f2a3e37c365f5926e1843bde13f47"
    url1 = f"http://api.openweathermap.org/data/2.5/weather?q={city1}&appid={api_key}"
    url2 = f"http://api.openweathermap.org/data/2.5/weather?q={city2}&appid={api_key}"
    
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    
    data1 = json.loads(response1.text)
    data2 = json.loads(response2.text)
    
    if data1["cod"] == 200 and data2["cod"] == 200:
        feels_like1 = data1["main"]["feels_like"]
        feels_like2 = data2["main"]["feels_like"]
        weather1 = data1["weather"][0]["main"]
        weather2 = data2["weather"][0]["main"]
        rain1 = data1.get("rain", {}).get("1h", 0)
        rain2 = data2.get("rain", {}).get("1h", 0)
        
        print(f"Comparison for {city1} and {city2}:")
        print(f"{city1} Feels Like: {feels_like1}K")
        print(f"{city2} Feels Like: {feels_like2}K")
        print(f"{city1} Weather: {weather1}")
        print(f"{city2} Weather: {weather2}")
        print(f"{city1} Rain: {rain1}mm")
        print(f"{city2} Rain: {rain2}mm")
    else:
        print("Error retrieving weather data for one or both cities. Please ensure that you typed in the name(s) properly.")

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
    city1 = get_city_input()
    city2 = get_city_input()
    compare_weather(city1, city2)
    
if __name__ == "__main__":
    main()