import requests
import json


class style:
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


url = 'http://api.weatherapi.com/v1/current.json'
KEY = '6027fbf90e994a9fbc2121452212101'
Q = 'Chernihiv'
parameters = {'key': KEY, 'q': Q}
response = json.loads(requests.get(url, params=parameters).content.decode())

city = f'{style.BLUE}{response["location"]["name"]},' \
       f'{response["location"]["country"]}{style.END}'
curr_temp = f'{style.DARKCYAN}{response["current"]["temp_c"]}{style.END}'
feels_like = f'{style.DARKCYAN}{response["current"]["feelslike_c"]}{style.END}'
wind_kph = f'{style.YELLOW}{response["current"]["wind_kph"]}{style.END}'
wind_dir = f'{style.RED}{response["current"]["wind_dir"]}{style.END}'

print(f'Місто:                {city}')
print(f'Поточна температура:  {curr_temp}, °C')
print(f'Відчувається як:      {feels_like}, °C')
print(f'Швидкість вітру:      {wind_kph}, км/год')
print(f'Напрям вітру:         {wind_dir}')
