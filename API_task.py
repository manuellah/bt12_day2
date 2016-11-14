import requests

def weather_checker(city):
    '''
    Will be using requests library as my http client library due to its ease of use.
    Will also use OPENWEATHERMAP api since its a public API and
    query and dispay the Temperature, Pressure and Humidity
    '''
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    payload = { 'q': city,
                "units": "metric",
                "appid": "2bc3e79bb974a007818864813f53fd35" 
              }
    r = requests.get(base_url, params = payload)
    data = r.json()
    pressure = data['main']['pressure']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
        
    return [temperature, humidity, pressure]
    
    
def main():
    dot = '--' * 30
    eqs = '==' * 30
    sign = u'\xb0'
    spacing = '\n\n\t'
    
    print '{}WELCOME TO OUR WEATHER CHECKER APP\n {}'.format(spacing, dot)
    city = raw_input("\n\t\tENTER THE CITY NAME  :  ")
    output = "{} The Current Tempuratures are {} Celcius, Humidity {}% and Pressure {}hPa".format(spacing, *weather_checker(city))
    print output.upper()
    
    print "{} {} Welcome Again\n\n".format(eqs, spacing)

    
if __name__ == '__main__':    
    main()