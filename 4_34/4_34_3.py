import requests

API_KEY = '093b91ab8417fd62cfdaf721ae372fe8'

while True:
    city = input("Enter a city: ")
    params = {'q': city,
              'appid': API_KEY}

    resp = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)

    if input == 'quit':
        break

    data = resp.json()

    if 'weather' in data.keys():
        result = {}
        result.update({'City': city})
        result.update({'Weather': data['weather'][0]['description']})
        result.update({'Temperature': data['main']['temp']})
        result.update({'Humidity': data['main']['humidity']})
    else:
        print('fail')
        result = data

    print(result)
