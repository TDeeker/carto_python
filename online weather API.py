#eb11325570e95d8884ab3386f8f0f46c

import requests

base_url = "http://api.openweathermap.org/data/2.5/weather?q="

APIK = input("APIK?")
city_name = input("quelle ville?")
city_name=(city)
print("Météo pour la ville de:"(city_name))
weather_data = requests.get(complete_url).json()
print(weather_data)
humidity_data=(weather_data['main']['humidity'])
requests.get(complete_url2).json()
print(humidity_data)

complete_url =  base_url + "appid=" + APIK + "&q=" + city_name +"&units=metric"

weather_data = requests.get(url).json()
ville=weather_data['name']
print("meteo à %s"%(ville))
print(weather_data['weather'][0]['description'])
print(weather_data['main']['temp'],"°C")