import requests

def get_weather(city):
    api_key = "api_key"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()

    if data.get("cod") != 200:
        return "City not found or API request failed."

    main = data["main"]
    weather = data["weather"]
    temperature = main["temp"]
    weather_description = weather[0]["description"]
    return f"The temperature in {city} is {temperature - 273.15:.2f}°C with {weather_description}."

def get_weather_map(layer, z, x, y, api_key):
    url = f"https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(f"{layer}_{z}_{x}_{y}.png", "wb") as file:
            file.write(response.content)
        return f"Weather map saved as {layer}_{z}_{x}_{y}.png"
    else:
        return "Failed to retrieve the weather map."
