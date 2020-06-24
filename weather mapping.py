import smopy
import requests
import matplotlib.pyplot as plt

APIK="eb11325570e95d8884ab3386f8f0f46c"

base_url="http://api.openweathermap.org/data/2.5/weather?q="


city = input("Enter a City:")

complete_url = base_url + city + "&appid=" + APIK +"&units=metric&lang=fr"

weather_data = requests.get(complete_url).json()

print(weather_data['main']['temp'], "°C")
print(weather_data['main']['humidity'],"%")

lat = weather_data['coord']['lon']
lng = weather_data['coord']['lat']
# On crée une MAP avec SMopy (basée sur les coord GPS de "city")
map = smopy.Map((lng, lat),z=8)


# on converti les coord GPS en pixels pour afficher sur l'image de la carte
# x et y seront les coordonnées dans l'image du point GPS :

x, y = map.to_pixels(lng,lat)

# je converti ma carte en image :
ax = map.show_mpl(figsize=(8, 6))

# j'ajoute un point de diam 10 et de bordure 2 en x,y
ax.plot(x, y, 'or', ms=10, mew=2)

# on ajoute une annotation
ax.annotate(weather_data['main']['temp'],
                    xy=(x,y), # coordonnés du libellé, ici même que le point
                    xytext=(3, 3), # décalage en X et Y du label
                    textcoords="offset points",  # in both directions
                    )
#on affiche
plt.show()