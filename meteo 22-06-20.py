import requests
import config

base_url="http://api.openweathermap.org/data/2.5/weather?appid="+config.apikey+"&units=metric"


def get_location():
    geocode=[]
    lonlat=open('C:/Users/T_Dee/Documents/Thomas Formation/lesson tech/lonlatonly.txt', 'r')
    for line in lonlat:
        lat,lon=line.split(",")
        coord={'ltt':lat.strip(),
                'lng':lon.strip(),}

        geocode.append(coord)
    return(geocode)

def print_dict(l,titre):
    print("==== %s ====" % titre)
    for item in l:
        print(item, " = ", l[item])

def get_area(locations):
    lat_min=lat_max=locations[0]['lat']
    lon_min=lon_max=locations[0]['lon']
    for location in locations:
        lat_min=min(lat_min, location['lat'])
        lat_max=max(lat_max, location['lat'])
        lon_min=min(lon_min, location['lon'])
        lon_max=max(lon_max, location['lon'])

    o_lat=((lat_max-lat_min)/100)*10
    o_lon=((lon_max-lon_max)/100)*10
    lat_min=lat_min-o_lat
    lat_max=lat_max+o_lat
    lon_min=lon_min-o_lon
    lon_max=lon_max+o_lon

    return{'lat_min':lat_min,'lat_max':lat_max,'lon_min':lon_min,'lon_max':lon_max}

def get_weather(c):
    lat=c['ltt']
    long=c['lng']
    url=base_url+"&lat="+lat+"&lon="+long
    print(url)
    data=requests.get(url).json()
    print(data)

def main():

    locations = get_locations('lonlatonly.txt')


    for location in locations :
        location = get_weather(location)

    area = get_area(locations)
    print_dict(area,"AREA")

    nbligne=0
    for location in locations :
        nbligne=nbligne+1
        sep = "LIGNE %d"  % nbligne
        print_dict(location,sep)



if __name__ == "__main__":
    main()