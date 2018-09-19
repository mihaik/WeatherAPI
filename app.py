import urllib.request
import json

def lookup(zip, country):
    api_key = '&&APPID=9b2c7c7f226d3ca9f0b2e55b07f0df22&units=imperial'
    url = 'http://api.openweathermap.org/data/2.5/weather?q='
    finalURL = url + zip + ',' + country + api_key

    response = urllib.request.urlopen(finalURL).read()
    jsonResponse = json.loads(response.decode('utf-8'))
    y = jsonResponse

    try:
        print('The city of ' + y['name'] + ', ' + country)
        print('Temp: ' + str(y['main']['temp']))
        print('Humidity: ' + str(y['main']['humidity']))
        print('Wind Speed: ' + str(y['wind']['speed']) + ' mph')

        for i in y['weather']:
            #print(i['main'])
            print('Cloud coverage: ' + i['description'])
    except ValueError:
        print('City does not exist')
        quit()



#country = input('Enter country. ')
zip = input('Enter zip. ')
#print(type(zip))

lookup(zip, country = 'us')