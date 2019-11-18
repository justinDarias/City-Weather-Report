import requests

API_ROOT = 'https://www.metaweather.com'
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/'  # + woeid

def fetch_location(query):
    return requests.get(API_ROOT + API_LOCATION + query).json()

def fetch_weather(woeid):
    return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()

def display_weather(weather):
    print('\nWeather for ' + weather["title"] + ':')
    for forecast in weather['consolidated_weather']:
        print("Date: " + forecast['applicable_date'])
        print("\t Tempurature: " + str(forecast['the_temp'] * 9/5 + 32) )
        print("\t Condition: " + forecast['weather_state_name'])
        print("\t Humidity: " + str(forecast['humidity']) + "%")

def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print("\t* " + loc['title'])

def weather_dialog():
    where = ''
    while not where:
        where = input("Where in the world are you? ")
    try:
        locations = fetch_location(where)
        if len(locations) == 0:
            print("I don't know where that is.")
        elif len(locations) > 1:
            disambiguate_locations(locations)
        else:
            woeid = locations[0]['woeid']
            display_weather(fetch_weather(woeid))
    except requests.exceptions.ConnectionError:
        print("Can't connect to server!")

if __name__ == '__main__':
    while True:
        weather_dialog()

#JustinArias
