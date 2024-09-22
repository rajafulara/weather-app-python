import requests

def get_weather(city):
    api_key = 'b1b15e88fa797225412429c1c50c122a1'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

city = input("Enter city name: ")
weather_data = get_weather(city)

if weather_data['cod'] == 200:
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    description = weather_data['weather'][0]['description']
    print(f'Temperature: {temperature}°C')
    print(f'Feels Like: {feels_like}°C')
    print(f'Weather: {description}')
else:
    print('City not found')
