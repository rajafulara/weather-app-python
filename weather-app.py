import requests

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

print('\n--- Weather app ---\n')

api_key = input('Enter openweather api key: ')
res = 'y'

while(1):
    if (res=='n'):
        break
    city = input('Enter city name: ')
    weather_data = get_weather(city)
    if (weather_data['cod'] == 200):
        temperature = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        description = weather_data['weather'][0]['description']
        country = weather_data['sys']['country']
        print('\n---\n')
        print(f'Country: {country}')
        print(f'City: {city}')
        print(f'Temperature: {temperature}°C')
        print(f'Feels Like: {feels_like}°C')
        print(f'Weather: {description}')
        print('\n---\n')
        res = input("Do you want another city's weather (y/n): ")
    else:
        print('\n---\n')
        print('City not found')
        print('\n---\n')
        res = input("do you want another city's weather (y/n): ")
