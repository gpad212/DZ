import requests
import json


#Задание 1
a = (requests.get("https://jsonplaceholder.typicode.com/posts")).json()
for i in range(5):
    print(f'Заголовок\n{a[i]['title']}')
    print(f'Тело\n{a[i]['body']}\n')

# Задание 2
#https://openweathermap.org/api не работает без vpn, сделал на яндекс погоде и с помощью яндекс карт

key_weather = 'token'
key_map = 'token'

headers = {
    'X-Yandex-Weather-Key': key_weather
}

city = input('Введите город: ')
response2 = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={key_map}&geocode=город+{city}&format=json').json()

a,b =response2['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()

query = "{weatherByPoint(request: { lat: " + b +", lon: " + a + " }) {now {temperature}}}"

response = requests.post('https://api.weather.yandex.ru/graphql/query', headers=headers, json={'query': query}).json()

print(response['data']['weatherByPoint']['now']['temperature'])