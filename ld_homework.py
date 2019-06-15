city = {
    'city': 'Москва',
    'temperature': 20
    }
print(city['city'])
city['temperature'] -= 5
print(city)
print(city.get('country', 'Россия'))
city['date'] = '27.05.2019'
print(len(city))
