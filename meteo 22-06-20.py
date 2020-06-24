import requests

api='eb11325570e95d8884ab3386f8f0f46c'

base_url="http://api.openweathermap.org/data/2.5/weather?appid="+api+"&units=metric"


def get_location():
    geocode=[]
    lonlat=open('C:/Users/T_Dee/Documents/Thomas Formation/lesson tech/lonlatonly.txt', 'r')
    for line in lonlat:
        lat,lon=line.split(",")
        coord={'ltt':lat.strip(),
                'lng':lon.strip(),
                }

        geocode.append(coord)
    return(geocode)

def get_weather(c):
    lat=c['ltt']
    long=c['lng']
    url=base_url+"&lat="+lat+"&lon="+long
    print(url)
    data=requests.get(url).json()
    print(data)

coords=get_location()
print(coords[0]);
get_weather(coords[0])