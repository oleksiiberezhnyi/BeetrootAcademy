import requests
import json


class Style:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


URL = 'http://api.weatherapi.com/v1/current.json'
KEY = '6027fbf90e994a9fbc2121452212101'
Q = 'Chernihiv'
parameters = {'key': KEY, 'q': Q}
response = json.loads(requests.get(URL, params=parameters).text)

city = f'{Style.BLUE}{response["location"]["name"]},' \
       f'{response["location"]["country"]}{Style.END}'
curr_temp = f'{Style.DARKCYAN}{response["current"]["temp_c"]}{Style.END}'
feels_like = f'{Style.DARKCYAN}{response["current"]["feelslike_c"]}{Style.END}'
wind_kph = f'{Style.YELLOW}{response["current"]["wind_kph"]}{Style.END}'
wind_dir = f'{Style.RED}{response["current"]["wind_dir"]}{Style.END}'

print(f'Місто:                {city}')
print(f'Поточна температура:  {curr_temp}, °C')
print(f'Відчувається як:      {feels_like}, °C')
print(f'Швидкість вітру:      {wind_kph}, км/год')
print(f'Напрям вітру:         {wind_dir}')
