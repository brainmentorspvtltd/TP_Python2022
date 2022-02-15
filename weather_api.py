Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request as url
>>> import json
>>> path = "https://api.openweathermap.org/data/2.5/weather?lat=28.6139&lon=77.2090&appid=83e01e3dce5d28839bb5a177cb51af12"
>>> response = url.urlopen(path)
>>> response
<http.client.HTTPResponse object at 0x0000023675A33E50>
>>> data = json.load(response)
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['coord', 'weather', 'base', 'main', 'visibility', 'wind', 'clouds', 'dt', 'sys', 'timezone', 'id', 'name', 'cod'])
>>> data.values()
dict_values([{'lon': 77.209, 'lat': 28.614}, [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}], 'stations', {'temp': 298.9, 'feels_like': 298.34, 'temp_min': 294.45, 'temp_max': 299.14, 'pressure': 1012, 'humidity': 31}, 3500, {'speed': 3.09, 'deg': 280}, {'all': 0}, 1644920117, {'type': 1, 'id': 9161, 'country': 'IN', 'sunrise': 1644888596, 'sunset': 1644928856}, 19800, 1260877, 'Parliament House, Delhi', 200])
>>> data['main']
{'temp': 298.9, 'feels_like': 298.34, 'temp_min': 294.45, 'temp_max': 299.14, 'pressure': 1012, 'humidity': 31}
>>> data['name']
'Parliament House, Delhi'
>>> data['weather']
[{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}]
>>> data['main']['temp']
298.9
>>> 