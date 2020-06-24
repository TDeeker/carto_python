import smopy
import requests
import matplotlib.pyplot as plt
import config

base_url='http://api.openweathermap.org/data/2.5/weather?q='

city = input("ta ville préférée?")

complete_url = base_url + city + "&appid=" + config.apikey +"&units=metric&lang=fr"

weather_data = requests.get(complete_url).json()

print("le meteo pour ta ville préférée:")
print(weather_data['main']['temp'], "°C")
print(weather_data['main']['humidity'],"%")

lat = weather_data['coord']['lon']
lng = weather_data['coord']['lat']

map = smopy.Map((lng, lat),z=8)

x, y = map.to_pixels(lng,lat)

ax = map.show_mpl(figsize=(8, 6))

ax.plot(x, y, 'or', ms=10, mew=2)

ax.annotate(weather_data['main']['temp'],
                    xy=(x,y),
                    xytext=(3, 3),
                    textcoords="offset points",
                    )
plt.show()